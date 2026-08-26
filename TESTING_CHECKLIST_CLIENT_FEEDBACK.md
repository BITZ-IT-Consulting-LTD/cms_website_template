# Testing checklist — Sauti client feedback round (branch `jun-changes`)

Nothing here has been run in a browser. All code compiles (every changed `.vue`
file was compiled by the running Vite dev servers, all Python files pass a
syntax check, migration dependency chains verified linear), but no behaviour has
been exercised. Work through this in order — **section 0 first**, or most of the
rest will fail for the wrong reason.

Dev URLs: public site `http://localhost:5173` · admin `http://localhost:5174`
· backend `http://localhost:8000` · nginx `http://localhost:8088`

---

## 0. Setup — do these first

1. **Rebuild the backend image.** `reportlab` was added to
   `sauti_cms/requirements.txt` for the PDF exports. Until the image is rebuilt,
   every export endpoint will 500 on import.
2. **Apply migrations.** Six new migrations across five apps, some hand-written:
   ```
   python manage.py makemigrations --check   # expect: no changes detected
   python manage.py migrate
   ```
   If `--check` reports missing migrations, a hand-written file doesn't match the
   models — stop and report which app before going further.
3. **Backfill image derivatives** (once, after migrating):
   ```
   cd sauti_cms && python backfill_image_derivatives.py
   ```
   Expect a "checked, N row(s) updated" line per model, no traceback.
4. **Reset the admin password if you can't log in.** An agent changed the seeded
   `admin` user's password during this session:
   `python manage.py changepassword admin`

---

## 1. Partner alternative phones and emails

1. Admin → **Partners** → **Add New Partner**. Name it `Manual Test Partner`.
2. Click **+ Add phone** twice (3 rows), enter three different numbers.
3. Click **+ Add email** once (2 rows), enter two different addresses.
4. Save. The new card should list all three phones and both emails.
5. **Persistence:** hard-refresh the page, reopen **Edit** on that partner —
   all 3 phone rows and both email rows must still be populated.
6. In the edit modal add a third email and delete the second phone. Save,
   refresh, reopen — expect 3 emails and 2 phones.
7. Open an older partner that only ever had a single phone/email — it should
   still display and edit correctly, with the single value in row 1.
8. Public site `/partners` — hover a partner card; every phone and email should
   appear as `tel:` / `mailto:` links, not just the first of each.

## 2. Contact item extra values

1. Admin → **Contact**, edit an item, add two **Additional values** via
   **+ Add another**, save, refresh, reopen — both must persist.
2. Public `/contact` — that channel should show the extra values as additional
   lines beneath the main entry, each linked correctly.

## 3. Social brand logos

1. Public `/contact` — Facebook, X, Instagram, YouTube, TikTok and WhatsApp must
   each show their **real coloured logo**, not a grey outline icon. Call, Email,
   SMS, Location and Portal keep the plain blue house icon.
2. Footer on any page — the social row should show the same coloured brand marks.

## 4. General feedback — wording, filter, downloads

1. Admin → **General Feedback**. Third stat card must read **Reviewed**, not
   "Resolved". No "Resolved"/"Resolve" wording anywhere on the page.
2. Click the **Archived** filter tab. URL becomes `?status=archived` and only
   archived messages show.
3. **Press F5.** It must stay on Archived, not bounce back to All/Pending.
4. Cycle Pending → Reviewed → All. Each tab's count must match the cards shown;
   "All" restores the three-group layout.
5. From Pending, click **Mark Reviewed** on a message — counts on every tab
   update immediately and the card leaves the Pending list.
6. From Archived, click **Unarchive** — must work from inside the filtered view.
7. Click the blue download icon on a card. A `feedback-<id>.pdf` downloads and
   opens, showing sender name, email, message, submitted date/time, status and
   reviewer. Try one with **no email** — it must print "Not provided", not blank.
8. With **Archived** active, click **Download All (CSV)**. Filename should
   contain `archived` and today's date, and contain only archived rows. Switch to
   **All** and download again — filename says `all`, every message included.

## 5. Case reports — downloads and full data visibility

1. Admin → **Reports** → **Download All (CSV)**. Opens as a spreadsheet, one row
   per report. Confirm there is **no** IP address, user agent, or encrypted
   description column.
2. Open any report → **Download PDF**. Confirm all fields plus Affected Persons
   and Follow-ups, "Not provided" for empties, and again no IP/user-agent.
3. **Submit the public form twice** at `/report`:
   - once answering **everything**, including the alternative contact question;
   - once **skipping every optional answer**.
4. Open both in the admin detail view. Check specifically that these now hold
   real values on the fully-answered one (they were being silently discarded
   before this change): **Alternative Contact**, **Victim / Affected-Person
   Location**, **Incident Type**.
5. On the skipped-answers report, every unanswered field must show a greyed
   italic **"Not provided"** — no hidden rows. Attachment, OpenCHS ID, Escalated
   At, Forwarded At and Resolved At must all be visible with placeholder text.
6. Confirm the description no longer starts with `[Incident Type: …]` on the new
   submissions, and that older reports which have that prefix still read fine.
7. Log out and request an export URL directly, e.g.
   `http://localhost:8000/api/reports/export/csv/` — must be rejected (401/403),
   not a download.

## 6. Resources — card layout and visibility

1. Admin → **Resources** at browser width **1920px**: each card shows two rows
   of buttons (View + Edit, then Download + Copy + Delete). Nothing may spill
   outside the card and the page must not scroll horizontally.
2. Repeat at **1440px**, **1280px** and a phone width (~375px).
3. Confirm Delete is not adjacent to Edit in the same row.
4. **Add New Resource** with Visibility = **Draft**. Card shows a yellow *Draft*
   badge; the resource must **not** appear on public `/resources`.
5. Edit it to **Published**, save, hard-refresh, reopen Edit — the dropdown must
   still read Published (persistence). Badge turns green; it appears publicly.
6. Set it to **Archived** — disappears publicly again, badge turns grey.
7. **Regression check:** edit an existing resource's *title only*, without
   picking a new file, and save. This previously failed with "No file was
   submitted" and should now succeed.

## 7. Article page — layout, gallery, dates, sharing

1. Admin → edit a News or Blog post. In the **Gallery** card, upload 3 images,
   give each a caption, reorder them, then save.
2. Reopen the post — all 3 images, captions and order must persist.
3. Public article page: layout should be a two-column article with a sticky
   sidebar (Share to + Related articles), collapsing to one column on mobile.
4. Gallery renders as a grid, not a carousel. Click an image — full-screen viewer
   opens with the caption. Test **Escape** to close, **←/→** to move between
   images, and that the page behind does not scroll while it is open.
5. Open an article with **no** gallery images — no empty "Gallery" heading or
   blank space should appear.
6. **Dates:** the byline must show an explicit date *and* time. Find a post with
   no `published_at` set — it must show its created date, never "Recently".
   Edit a post and confirm an "Updated …" line appears.
7. **Related articles:** click one in the sidebar. It must load that article
   (this was a 404 before — the links pointed at `/blog/` not `/blogs/`), and the
   content must actually change rather than showing the previous article.
8. **Search box** (top right of the article page): type a term and press Enter.
   It should land on `/news` or `/blogs` with `?search=<term>` and the results
   already filtered.
9. **Share sidebar:** Facebook, X, WhatsApp, LinkedIn, Telegram and Email each
   open the right composer with the article's URL. The copy button flips to a
   checkmark. The Instagram/TikTok line opens the device share sheet on mobile,
   or copies the link with a "paste it into Instagram or TikTok" message.

## 8. Resource sharing and link previews

1. Public `/resources` — each card now has a share row. Click copy-link; it
   should confirm.
2. Paste that URL (`/resources?resource=<slug>`) into a new tab — the page should
   scroll to that card and ring-highlight it.
3. **The preview itself** (the original complaint). This needs the crawler route
   deployed — see section 9. Once it is, paste an article link into WhatsApp and
   confirm a card with that article's own title, description and image appears
   instead of plain text. Verify with the Facebook Sharing Debugger too.
4. Note: share links now come from `VITE_PUBLIC_BASE_URL`. It is deliberately
   **empty in dev**, so locally you'll get `localhost` URLs — that's expected.
   Production is set to `https://sauti.mglsd.go.ug/sauti`.

## 9. Crawler OG route — REVIEW BEFORE DEPLOYING

This is the one change I would not push without testing on the server.

1. `python manage.py check` should pass with the new `seo` app wired at
   `api/seo/`.
2. Restart the backend, then hit
   `http://localhost:8000/api/seo/post/<published-slug>/` — expect HTML
   containing that post's real `og:title` / `og:image`, and a 404 for a bad slug
   or a draft post.
3. **Run `nginx -t` against every changed config before deploying:**
   `docker/nginx/dev.conf`, `prod.conf`, `host-nginx.conf`,
   `host/sauticms/cms_logic.inc`. There is no nginx binary in my environment, so
   these are unverified. Note `host-nginx.conf` and `cms_logic.inc` are **live
   production host configs** — treat those two as the risky ones.
4. Simulate a crawler and a human against the same URL:
   ```
   curl -A "WhatsApp/2.0" http://localhost:8088/blogs/<slug>   # expect OG HTML
   curl -A "Mozilla/5.0"  http://localhost:8088/blogs/<slug>   # expect the SPA
   ```

## 10. Image loading performance

1. After the backfill, edit a Post and upload a large `featured_image`. Check
   `http://localhost:8000/api/posts/<slug>/` returns non-null
   `featured_image_thumbnail` and `featured_image_medium`.
2. Public site, DevTools → Network → **Img**. Reload the homepage: card and logo
   requests should point at `.../thumbnails/...` paths, with noticeably smaller
   sizes than the originals.
3. On `/about` and `/operations`, hard-reload and confirm only visible images
   load immediately; the rest fire as you scroll (staggered waterfall).
4. Rendering tab → **Layout Shift Regions**, reload — no shift regions around
   images as they arrive.
5. Pick a row created before the backfill and confirm the page still shows an
   image (falls back to the original), not a broken-image icon.
6. Click a `/media/` request → Response Headers → confirm `Cache-Control` /
   `Expires` reflects the ~30-day value, and a second visit serves from cache.
7. **Regression check for a bug this repo has hit before:** upload a new *video*
   thumbnail in the admin and confirm it actually saves.

---

## Known gaps and honest caveats

- **No performance number.** Local media is 2.2 MB, too small to reproduce the
  reported slowness, so the derivative work is the right fix for the likely cause
  (full-resolution originals used as card thumbnails) but its real-world effect
  is unmeasured. Measure on production before reporting back to the client.
- **`nginx -t` never run** — section 9.
- **OperationsPage's 12 external Unsplash images** are untouched. They already
  carry sizing params, but they are still a third-party latency source.
- **`BlogPost.vue`** was updated but is not imported by any route, so changes
  there have no visible effect.
- **Admin gallery editor** is still a stacked row list, not a drag-to-reorder
  thumbnail grid. Fine for a few images, awkward at twenty.
- **Nothing is committed.** All of the above is uncommitted working-tree changes.
