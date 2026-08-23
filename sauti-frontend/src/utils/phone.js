/**
 * Shared phone-number normalisation helpers.
 *
 * wa.me links require the full international number in E.164 form WITHOUT
 * a leading '+' (e.g. '256743889999'). CMS-managed Contact records are
 * frequently entered in Uganda local format (e.g. '0743889999'), which
 * would otherwise produce a dead wa.me link if only non-digit characters
 * were stripped.
 */

// Known-good default, matches the historical hardcoded WhatsApp number.
const FALLBACK_WA_NUMBER = '256743889999'

/**
 * Normalise a raw phone number into the digits-only, international
 * (country-code-prefixed, no '+') format that wa.me links require.
 *
 * Rules:
 *  - Strip spaces, dashes, parens, '+', and any other non-digit characters.
 *  - A number that was given with a leading '+' is assumed to already carry
 *    an explicit (possibly non-Ugandan) country code — pass it through as
 *    digits only, untouched.
 *  - Already-international Uganda format ('256XXXXXXXXX') — used as-is.
 *  - Uganda local format with a leading '0' ('0XXXXXXXXX') — the leading
 *    '0' is replaced with '256'.
 *  - A bare 9-digit subscriber number with no leading '0' or country code
 *    ('XXXXXXXXX') — '256' is prefixed.
 *  - Any other longer number that doesn't match the above (no '+', no '0'
 *    or '256' prefix, more than 9 digits) is assumed to carry some other
 *    country code already — passed through as digits only, NOT forced
 *    into a '256' prefix.
 *  - Anything empty/unusable falls back to the known-good default.
 *
 * Defensive: never throws, never returns an empty string.
 *
 * @param {*} raw
 * @returns {string}
 */
export function toWaMeNumber(raw) {
  try {
    if (raw === null || raw === undefined) return FALLBACK_WA_NUMBER

    const str = String(raw).trim()
    if (!str) return FALLBACK_WA_NUMBER

    const hadPlus = str.startsWith('+')
    const digits = str.replace(/\D/g, '')

    if (!digits) return FALLBACK_WA_NUMBER

    // Explicit international number (had a leading '+') — trust the
    // country code the admin entered, don't reinterpret it as Ugandan.
    if (hadPlus) return digits

    // Already international Uganda format.
    if (digits.startsWith('256')) return digits

    // Uganda local format with leading trunk '0'.
    if (digits.startsWith('0')) return `256${digits.slice(1)}`

    // Bare 9-digit Ugandan subscriber number (no leading '0', no country code).
    if (digits.length === 9) return `256${digits}`

    // Longer number without a recognised Uganda prefix — likely already
    // carries a different country code; don't force '256' onto it.
    if (digits.length > 9) return digits

    return FALLBACK_WA_NUMBER
  } catch (e) {
    return FALLBACK_WA_NUMBER
  }
}

export default toWaMeNumber
