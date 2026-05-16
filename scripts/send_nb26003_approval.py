"""Send NB26-003 Khun Nan order confirmation for customer signature.

Usage:
    python scripts/send_nb26003_approval.py --to "customer@email.com" [--cc "cc@email.com"]

Requires:
    - WeasyPrint:  pip install weasyprint
    - Google auth: ADC (gcloud auth application-default login) or SA key
    - go-documents src/ on sys.path (run from project root)

The script:
1. Reads the HTML order confirmation from Google Drive
2. Renders it to PDF via WeasyPrint
3. Emails it via Gmail DWD (eukrit@goco.bz) with the acceptance clause
4. Applies the Submissions/Materials Gmail label
"""
from __future__ import annotations

import argparse
import sys
import os
from datetime import datetime, timezone
from pathlib import Path

# ── allow imports from src/ when run from project root ──────────────────────
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

# ── config ───────────────────────────────────────────────────────────────────
ORDER_REF    = "NB26-003"
PROJECT_NAME = "Khun Nan Private Residence"
CUSTOMER     = "Khun Nan"

# Adjust this path if the HTML file lives elsewhere on your machine
HTML_SOURCE  = Path(
    r"C:\Users\Eukrit\My Drive\Sales Order GO\Sales Order 2026 Nubo"
    r"\NB26-003 Khun Nan Mattress (Wait for confirmation)"
    r"\NB26-003-Order-Confirmation.html"
)

PDF_FILENAME = "NB26-003-Order-Confirmation-Khun-Nan.pdf"


def render_pdf(html_path: Path) -> bytes:
    try:
        from weasyprint import HTML
    except ImportError:
        raise RuntimeError(
            "WeasyPrint not installed. Run: pip install weasyprint"
        )
    html_str = html_path.read_text(encoding="utf-8")
    # WeasyPrint resolves relative URLs against base_url
    return HTML(string=html_str, base_url=str(html_path.parent)).write_pdf()


def main():
    parser = argparse.ArgumentParser(
        description="Email NB26-003 order confirmation to Khun Nan"
    )
    parser.add_argument("--to",  required=True,  nargs="+", help="Recipient email(s)")
    parser.add_argument("--cc",  default=[],      nargs="*", help="CC email(s)")
    parser.add_argument("--bcc", default=[],      nargs="*", help="BCC email(s)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Render PDF only; don't send email")
    args = parser.parse_args()

    print(f"[1/3] Rendering PDF from {HTML_SOURCE} ...")
    if not HTML_SOURCE.exists():
        sys.exit(f"ERROR: HTML file not found at {HTML_SOURCE}")
    pdf_bytes = render_pdf(HTML_SOURCE)
    print(f"      PDF rendered — {len(pdf_bytes):,} bytes")

    if args.dry_run:
        out = Path(PDF_FILENAME)
        out.write_bytes(pdf_bytes)
        print(f"[dry-run] PDF saved to {out.resolve()} — email NOT sent.")
        return

    print(f"[2/3] Importing go-documents gmail_sender ...")
    from gmail_sender import send_submission_email

    # Build a minimal submission dict so the acceptance clause renders
    submission = {
        "submissionId": ORDER_REF,
        "type":         "material",
        "soRef":        ORDER_REF,
        "projectName":  PROJECT_NAME,
        "revision":     "00",
        "submissionType": "Initial",
        "responseDays": 5,
    }

    subject = (
        f"[{ORDER_REF}] Order Confirmation — {PROJECT_NAME} — "
        f"Visconti Future 1# Mattresses (5 units) — Please sign and return"
    )

    body = (
        f"Dear {CUSTOMER},\n\n"
        f"Thank you for your order. Please find attached the Order Confirmation "
        f"for {ORDER_REF} — {PROJECT_NAME}.\n\n"
        f"The document confirms:\n"
        f"  • 1× Visconti Future 1# 150×200 cm (Firmness 4 FIRM, Fabric A)\n"
        f"  • 4× Visconti Future 1# 180×200 cm (Firmness 4 FIRM, Fabric A)\n"
        f"  • Sea freight, clearance, tax & installation\n"
        f"  • Total: USD 52,336.80\n\n"
        f"Kindly review, sign, and return the document at your earliest convenience. "
        f"Production will commence upon receipt of the 70% deposit (USD 36,635.76).\n\n"
        f"Please sign and date the document where indicated and reply to this email "
        f"with the signed copy attached.\n\n"
        f"Bank details for deposit:\n"
        f"  Account Name : Nubo International Pte. Ltd.\n"
        f"  Bank         : OCBC Bank, Singapore\n"
        f"  Swift        : OCBCSGSG\n"
        f"  Account No.  : 517734174201\n\n"
        f"For questions, contact:\n"
        f"  Edmund Lim  +65 9191 1192  edmund@nubo.sg\n"
        f"  Eukrit       +66 61 491 6393  eukrit@nubo.sg\n\n"
        f"Best regards,\n"
        f"Nubo International Pte. Ltd.\n"
    )

    print(f"[3/3] Sending email to {args.to} ...")
    msg_id = send_submission_email(
        submission=submission,
        pdf_bytes=pdf_bytes,
        pdf_filename=PDF_FILENAME,
        attachments=[],
        to=args.to,
        cc=args.cc or None,
        bcc=args.bcc or None,
        subject=subject,
        body_text=body,
        include_acceptance_clause=True,
    )
    print(f"      Email sent — Gmail message id: {msg_id}")
    print(f"\nDone. {ORDER_REF} order confirmation sent to {', '.join(args.to)}.")


if __name__ == "__main__":
    main()
