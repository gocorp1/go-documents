# Changelog

All notable changes to this project will be documented in this file.

## [1.4.3] - 2026-05-28 — CR-2026-001 final: Compliant verdict + SO25-056 project reference

Reviewer (Eukrit, CPSI 64835-0801) performed both in-field checks:
1. F1487 §6.3 — projection gauge test (1.25 in. / 2.0 in. / 3.5 in. OD) on every accessible head: **Pass**
2. F1487 §6.4.3 — rear-face thread protrusion ≤ 2 full threads beyond nut: **Pass**

With both checks confirmed, the conditional pass is upgraded to an unconditional pass.

- **Verdict:** `Conditional Pass` (amber) → `Compliant` (green). `class="verdict conditional"` → `class="verdict"`.
- **Identification grid:** added `Project / Site: SO25-056 Dusit Residence`. `Review Type` updated to "Photographic + in-field verification by reviewer (CPSI)". Issue date bumped to 2026-05-28.
- **Clause table:** four rows flipped Verify/N/A → Pass with reviewer-attested observations:
  - §6.3 projection gauge — Pass (head does not extend beyond any gauge face)
  - §6.4.3 exposed bolt-end — Pass (rear face inspected; ≤ 2 threads)
  - §8.11.2 spring rocker handgrip — Pass (fasteners pass §6.3 above)
  - LEKA-STD-PLAY-001 §5.3 — Pass (in-field gauge test passed)
- **Findings:** F-2 / F-3 rewritten as "verified — passed".
- **Risk classification:** F-2 / F-3 pending lines removed; F-1 / F-2 / F-3 collapsed to a single Class IV (no risk).
- **Remediation section retitled "Preventive Maintenance":** the three remediation items collapse to a single preventive line P-1 (add the head + thread check to the monthly / quarterly inspection list per LEKA-STD-PLAY-001 §11).
- **References:** added the project line `Project — SO25-056 Dusit Residence` at the top.

## [1.4.2] - 2026-05-28 — CR-2026-001 correction: protective cap is not required

Correction after user re-review (Eukrit, CPSI 64835-0801) of v1.4.1.

**Issue:** v1.4.0/v1.4.1 incorrectly treated the rubber overmould of the U-handle as a removable "protective cap" and flagged a Class III "cap displacement" finding (F-2). Re-reading the photo and the standard:

- ASTM F1487-17 does **not** require a protective cap. A smooth, domed (round / button) head with no sharp edges and no size-increasing shoulder satisfies §6.2.1, §6.3 (projection gauge), §6.4.4 (mushroom rule) and §8.11.2 on its own.
- CPSC #325 §5.3.5.2 lists "flush **or** covered with caps" as **parallel** acceptable options &mdash; the conjunction is "or", not "and". A smooth dome head is itself flush.
- The black material around each bolt head is the rubber overmould of the U-handle terminating against the panel, not a separate protective cap that can slip.

**Changes:**
- Verdict body rewritten: pass is now conditional only on the in-field projection gauge test (F-2) and rear-face thread inspection (F-3). Cap language removed.
- Clause-by-clause table: CPSC #325 §5.3.5.2 row reclassified Pass (flush dome meets the "or" branch). F1487 §13.1 maintenance row reclassified Pass (no defect observed).
- Findings: F-2 ("cap seating") deleted as a misread. Former F-3 / F-4 renumbered to F-2 / F-3.
- Risk classification: F-2 Class III removed. F-1 stays Class IV.
- Remediation: R-1 / R-2 (cap reseat) removed. Former R-3 / R-4 / R-5 renumbered; R-3 reframed as a general fastener-head + thread check, not a cap-retention check.

## [1.4.1] - 2026-05-28 — CR-2026-001 final reviewer credentials + evidence photo

Patch on top of v1.4.0 to make the report a finished, signable document.

- `docs/reports/compliance/CR-2026-001-round-head-bolt-spring-rocker.html` — replaced `[Reviewer Name]`, `[CPSI #]`, `[YYYY-MM-DD]` placeholders with real values:
  - Reviewer: **Eukrit Kraikosol**
  - CPSI Certificate No.: **64835-0801**
  - CPSI Expiration Date: **2028-08-01**
  - (Source: `2026 Chachoengsao Claude/scraped/cpsi_certificates/F0B1BN2R1NH__PDF_output Eukrit CPSI Certificate.pdf`)
- `images/findings/CR-2026-001-spring-rocker-bolt.jpg` — added the actual evidence photograph (393 KB JPG; converted from the original WebP). The graceful `<img onerror>` placeholder fallback now no longer triggers.
- `gateway-pages.json` — registered the new image path with `visibility: "public"` (seeded into Firestore `ai-agents-go/gateway-access`). The HTML report and its embedded asset are both publicly viewable; both remain excluded from `docs/hub.html` per Rule 14.

## [1.4.0] - 2026-05-26 — Compliance Review CR-2026-001 (round-head bolt, spring rocker handle)

Added the first **Component Compliance Review** in the new `docs/reports/compliance/` directory, applying the Leka Studio design system to a focused 2-page A4 deliverable.

- `docs/reports/compliance/CR-2026-001-round-head-bolt-spring-rocker.html` — clause-by-clause analysis of a round-head (button-head) machine fastener exposed at a spring rocker handle attachment, against **ASTM F1487-17** §6.2.1 (sharp edges), §6.2.4 (cut-off bolt end), §6.3 (protrusion / projection-gauge test), §6.4.3 (exposed bolt-end / 2-thread rule), §6.4.4 (size-increasing projection), §7.2.6.4 (hand-gripping), §8.11.2 (spring rocker handgrips), §13 (maintenance); **CPSC Pub. #325** §5.3.5.2 (owner hardware guidance); and the new `leka-standards` consolidated standard `LEKA-STD-PLAY-001 v1.0` §5.3 and §13. Verdict: **Conditional Pass** — design selection is compliant; one protective cap appears partially displaced and requires reseating; in-field projection-gauge verification required.
- New report subfolder: `docs/reports/compliance/` for future component compliance reviews.
- New image subfolder: `images/findings/` (gitkeep-style; report references `CR-2026-001-spring-rocker-bolt.jpg` with graceful placeholder fallback if missing).
- All cross-references point to the canonical sources at `leka-standards/docs/sources/` (extracted PDF text) and `leka-standards/docs/standards/leka-playground-safety-standard.md`.

Served via gateway at `https://gateway.goco.bz/go-documents/docs/reports/compliance/CR-2026-001-round-head-bolt-spring-rocker.html`.

## [1.3.4] - 2026-05-19 — Safety: auto-commit drift guard + machine-local gitignore patterns

Ported from `data-communications` v0.5.14 (go-access-gateway v0.6.9 lineage). Closes the loop on the 2026-05-17 OneDrive-de-sync class of incident.

- `scripts/auto-commit-and-merge.sh` — new "Drift sanity check" section between the repo-mapping check and verify; hard-aborts on race / machine-fork / git-internals patterns (`DRIFT_RE`); skipped under `--paths`.
- `.gitignore` — defense-in-depth Rule-5 patterns (`.claude/autocommit.opt-in[.*]`, `.claude/active-machine.*`, `.claude/scheduled_tasks.lock`, `.claude/autocommit.opt-out`, `.claude/session-state.*`, `.git-*.archived-*`, `.git.broken-*`, `.git-*.bak.*`, host-suffix race duplicates).
- Removed working-tree Rule-5 violations: per-machine opt-in markers, `.git-NCORE100.bak.2026-05-08/` (archived git dir), and `cloudbuild-NCORE100.yaml` (an older, less-complete fork — tracked `cloudbuild.yaml` already has 3 more env vars).

## [1.3.3] - 2026-05-04

### Added — Signature Service workflow summary page
- New page `docs/summaries/signature-service.html` covering the end-to-end
  submission sign-off workflow: bilingual EN+TH deemed-accepted clause
  (7 working days), Google Drive native eSignature workflow (manual UI step),
  Slack interactivity fan-out via slack-router with `submission_*` action_id
  prefix routing, full stack summary, and configuration reference.
- Reachable via the gateway at
  `https://gateway.goco.bz/go-documents/docs/summaries/signature-service.html`
  after Google sign-in (admin visibility, eukrit@goco.bz).
- Hub regenerated to surface the new summary in the project hub.

(Originally added under go-access-gateway in that repo's v0.6.3, but moved
here in v0.6.3.1 of go-access-gateway because go-access-gateway itself was
not registered as a project in the gateway's project DB.)

## [1.3.2] - 2026-04-26

### Changed — Drive folder ID + Slack signing secret auto-load

- `src/drive_upload.py` — switched from name-resolution ("GO Submissions"
  Shared Drive lookup) to a hardcoded Drive folder ID with env override.
  Default points at the **"Submissions GO"** folder Eukrit pre-created
  (`1gAhGAI94Z96aFUm3nCp66QO573ixm-Vh`). Override via
  `SUBMISSIONS_DRIVE_FOLDER_ID` env. Works for both Shared Drive subfolders
  and My Drive folders via `corpora=allDrives` + `supportsAllDrives=True`.
- `src/app.py` — `_verify_slack_signature` now falls back to Secret Manager
  (`slack-signing-secret` in `ai-agents-go`) when `SLACK_SIGNING_SECRET` env
  is unset. Same pattern as `slack_notifier._get_token()` for the bot token.
  Cached in-process. Override secret name via `SLACK_SIGNING_SECRET_NAME`.

### Operations checklist (replaces v1.3.1 manual env-var step)
- ~~Set `SLACK_SIGNING_SECRET` env on go-documents Cloud Run~~ — no longer
  required; auto-loaded from `slack-signing-secret` GSM secret. Verify the
  go-documents runtime SA has `roles/secretmanager.secretAccessor` on it.
- DWD scope `drive.file` still required for `claude@ai-agents-go`.
- `eukrit@goco.bz` (the impersonated user) needs Editor access on the
  "Submissions GO" folder. Since Eukrit created it, this is already the case.

## [1.3.1] - 2026-04-26

### Changed — Slack Router wiring corrected

The "Slack Router" in `data-communications/slack-router/` is the **incoming
interactivity dispatcher**, not an outgoing channel-resolver. v1.3.0 wired
`slack_notifier.py` to a non-existent `route_event` HTTP endpoint based on a
misread of upstream. v1.3.1 corrects this:

- `src/slack_notifier.py` restored to hardcoded channel posting (legacy
  behaviour) but the card now carries **interactive Approve / Reject /
  Comment buttons** with `submission_*` `action_id` prefixes.
- New `/slack/interactivity` endpoint in `src/app.py` — receives button
  clicks forwarded by the slack-router service, verifies Slack signature
  via `SLACK_SIGNING_SECRET`, dispatches `submission_approve_*` /
  `submission_reject_*` / `submission_comment_*` to update the submission
  status and publish a `status_changed` Pub/Sub event (which fans out to
  Slack again as a status-update card).
- `data-communications/slack-router/routes.json` — new rule routing
  `submission_*` action_id prefix to `https://docs.leka.studio/slack/interactivity`.
- `data-communications/src/routing_engine.py` — added `submission_material` /
  `submission_drawing` to `_FALLBACK_SUBCATEGORY_MAP` so organic email
  classification (e.g. consultant replies referencing a submission) lands in
  the right channel without Firestore config bootstrap.

### Operations checklist (additions to v1.3.0)
- Set `SLACK_SIGNING_SECRET` env on go-documents Cloud Run (same secret as
  slack-router uses; from the GoCo Slack app config).
- Redeploy `slack-router` Cloud Run service to pick up the new
  `routes.json`. (Existing Slack app interactivity URL is already pointed
  at slack-router — no Slack-app-config change needed.)

## [1.3.0] - 2026-04-26

### Added — submission sign-off (clause + Drive eSignature)

- **Bilingual "Acceptance & Response Period" clause** (EN + TH) appended to every
  submission PDF AND every submission email body. Default 7 working days,
  configurable via `SUBMISSION_RESPONSE_DAYS` env var. If no written comments are
  received in that window, the submission is deemed accepted in full.
  Single source of truth: `src/submission_clause.py`.
- **Templates:** new `<!-- ACCEPTANCE_CLAUSE -->` marker + `.limitations.acceptance`
  styling in both `docs/reports/material-submission-template.html` and
  `docs/reports/drawing-submission-template.html`.
- **Email injection:** `gmail_sender.send_submission_email` now appends the clause
  to default and override `body_text`. Opt-out via `include_acceptance_clause=False`.
- **Google Drive eSignature workflow:** new `src/drive_upload.py` mirrors every
  rendered PDF to Shared Drive `GO Submissions/Submissions/<soRef>/<sid>.pdf` via
  DWD impersonation. `driveFileId` + `driveWebViewLink` persisted on the
  submission record. PMs click "Request signature" in Drive UI for native
  Workspace eSignature. (No public API yet — manual step.)
- **Slack notification card** carries Open + Drive (Sign) URL buttons
  (status-page + Drive web-view link). v1.3.1 adds Approve / Reject /
  Comment buttons routed via slack-router (see v1.3.1 entry above).

### Changed
- `src/submission_render.py` — `TEMPLATES` now reads from `docs/reports/`
  (Rule 13 docs-only layout) instead of repo root.
- `src/firestore_submissions.mark_sent()` — accepts `drive_file_id` /
  `drive_web_view_link`.

### Operations checklist (manual, post-deploy)
- Create Shared Drive **"GO Submissions"** in Workspace; add
  `claude@ai-agents-go.iam.gserviceaccount.com` as Content Manager.
- Grant DWD scope `https://www.googleapis.com/auth/drive.file` to
  `claude@ai-agents-go` in Workspace admin (existing scopes:
  `gmail.send`, `gmail.modify`, `gmail.labels`).
- Create Secret Manager secret `data-comms-router-token` with a random 32-byte
  value; grant `roles/secretmanager.secretAccessor` to the data-communications
  AND go-documents runtime SAs.
- Deploy data-communications: `gcloud functions deploy route_event ...`.
- Update go-documents Cloud Run service env: set `SLACK_ROUTER_URL` to the
  deployed function URL.

## [1.2.0] - 2026-04-24

### Added — material + drawing submission workflow
- **Templates:** `docs/reports/drawing-submission-template.html` (clone of material template
  with drawing-specific fields: Discipline, Issue Purpose, Drawn By, Checked By;
  Drawing List table with Drawing No / Title / Rev / Scale / Sheet Size;
  attachments list for PDFs / CAD / model / calcs).
- **Firestore:** new `submissions` collection (database `go-documents`). Doc id
  scheme `MS-<SO>-NNN` / `DS-<SO>-NNN`. See `src/firestore_submissions.py` for
  models, id generation, CRUD, and `list_so_refs()` dashboard aggregation.
- **App endpoints (`src/app.py`):**
  - `POST /api/submissions` — create a material or drawing submission
  - `POST /api/submissions/<id>/attachments` — upload file → GCS
    `go-documents-files/submissions/<id>/attachments/<filename>`
  - `POST /api/submissions/<id>/send` — render PDF, fetch recipients via
    `project_email_loops.get_recipients(soRef)`, send via Gmail as
    `eukrit@goco.bz` (DWD), apply Submissions label, publish Pub/Sub event
  - `PATCH /api/submissions/<id>/status` — update approval status
  - `GET /submissions/<id>` — view filled HTML · `/submissions/<id>/pdf` — PDF
  - `GET /dashboard` — master project directory (all SO refs with counts)
  - `GET /projects/<soRef>` — per-project submission dashboard
  - `POST /pubsub/push` — Pub/Sub push receiver → Slack fan-out
- **Gmail:** `src/gmail_sender.py` — DWD-impersonated send as `eukrit@goco.bz`,
  applies `Submissions/Materials` or `Submissions/Drawings` label on the sent
  message via `messages.modify` (filters can't reliably match outgoing).
- **PDF render:** `src/submission_render.py` — WeasyPrint-based server-side PDF
  render from the HTML templates (no headless Chromium).
- **Events:** `src/submission_events.py` publishes to Pub/Sub topic
  `submission-events` on created/sent/status_changed. `src/slack_notifier.py`
  posts to `#submission-materials` / `#submission-drawings` with an Open button
  linking back to `/submissions/<id>`.
- **Setup scripts:**
  - `scripts/setup_gmail_labels.py` — create `Submissions/Materials` and
    `Submissions/Drawings` labels on eukrit@goco.bz
  - `scripts/setup_pubsub.sh` — create topic + push subscription to Cloud Run
    `/pubsub/push`, wire SA as invoker
  - `scripts/setup_slack_channels.py` — create `#submission-materials` and
    `#submission-drawings` public channels
- **Deploy:** Dockerfile bumped to install Pango/HarfBuzz/libjpeg for
  WeasyPrint; Cloud Run memory raised to 1Gi, env vars `GCP_PROJECT`,
  `SUBMISSION_SENDER`, `SUBMISSION_EVENTS_TOPIC` set.

### Changed
- `src/app.py` — root `/` now redirects to `/dashboard`; submission viewer
  prefers new `submissions` collection, falls back to legacy `document-records`.

### Prerequisites (must be done once by owner)
- Grant DWD on `claude@ai-agents-go` SA for scopes `gmail.send`,
  `gmail.modify`, `gmail.labels` (Workspace admin console).
- `scripts/setup_pubsub.sh` must run after first Cloud Run deploy so the push
  URL resolves.

## [1.1.0] - 2026-04-22

### Added — project email-loop lookup
- `src/project_email_loops.py` — reads `go_project_email_loops` collection
  from the `go-sales-orders` Firestore database at document-submission time.
  Exposes `get_loop(so_ref)` (full doc) and `get_recipients(so_ref, *,
  internal_only, external_only, min_confidence)` (flat to/cc/bcc email lists)
  with `min_confidence` defaulting to `MEDIUM` so LOW-confidence Gmail
  backfill rows are excluded from real sends.
- Collection schema and population scripts live in the `go-sales-orders`
  project: `create_email_loops_collection.py` (manual) and
  `backfill_email_loops.py` (Gmail-driven).

## [1.0.0] - 2026-04-08

### Added
- Firestore database `go-documents` (asia-southeast1)
- `document-templates` collection with `areda-quotation` template schema
- `document-records` collection (migrated from `areda_quotations`)
- `document_counters` collection for running number generation
- AQ-26001: ED 70 Aluminum Folding Door quotation (EN + TH)
- AQ-26002: OPK Multi-Panel Folding Wooden Door Hardware System quotation (EN + TH)
- Quotation HTML templates (EN + TH) with Areda design system
- Pydantic models for document records (`src/firestore_models.py`)
- Firestore CRUD + running number generation (`src/firestore_quotations.py`)
- China-Thai freight calculator (Gift Somlak confirmed rates)
- Migration script from `areda-product-catalogs` DB to `go-documents` DB
- Product images extracted from OPK supplier Excel
- CI/CD infra from goco-project-template (Dockerfile, cloudbuild, scripts)
- GitHub repo: `eukrit/go-documents`

## [0.1.0] - 2026-03-24

### Added
- Initial project template with CI/CD pipeline
