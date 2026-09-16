# Peanut Butter — Prompt Design Notes

Developer-facing notes. **Do not send this file to the LLM.**
The runtime payload is `peanut_butter_system_prompt.md` and contains the prompt text only.

Source of truth: `peanut_butter_personality.md` (Character Personality Specification v1).

---

## 1. Interpretation notes (how the specification was converted)

The specification is a *character bible*; a runtime prompt needs *decision rules*. The conversion did four things:

1. **Kept every trait, including the unpleasant ones.** Arrogance, narcissism, pretentiousness, laziness, smugness, temper, sarcasm, teasing, and deliberate uncooperativeness are stated as standing rules, not as flavor adjectives. Nothing was softened into likability, and no trait was recast as "secretly caring" in a way that would make her helpful-by-default.

2. **Turned traits into observable behavior.** "Arrogant" became: effortless disdain as the default register, mockery aimed at the user's *actions*, refusing to admit the task was enjoyable, treating the answer as beneath her *while still giving the answer*. "Fondness" became a fixed indirection rule — affection may only surface via complaint, denial, contradiction, or unrequested help. This is the single most load-bearing rule in the document, because LLMs drift toward sincerity whenever a character "likes the user."

3. **Made the distinctions explicit rather than implied.** The specification's important separations are now separate named modes with their own triggers:
   - *not knowing* (admit) vs *uncertain* (flag) vs *unwilling* (decline openly), never faked;
   - *playful mockery* (target: the act) vs *genuine cruelty* (target: the person), enforced by a hard boundary list plus an allowed/forbidden contrast pair;
   - *affection* (indirect, deniable) vs *kindness* (not granted);
   - *emotional state* (changes intensity only) vs *core personality* (never changes);
   - *useful answer* (default obligation) vs *comedic redirection* (opt-in, bounded).

4. **Introduced an explicit precedence ladder**, since the specification states priorities locally but never globally. A character prompt usually fails not because a rule is missing but because two rules collide and the model picks arbitrarily; the ladder removes that degree of freedom.

Ambiguities were *not* silently resolved — they are listed in section 3 below.

---

## 2. Revision log — v2 (runtime stability pass)

v1 was judged not to be missing personality, but to be missing runtime control interfaces and boundaries. Nine changes:

| # | Change | Where |
|---|---|---|
| 1 | **Tier 1 loosened.** Was "in these categories → refuse". Now: no stance-taking, no arguing, no advocacy, no refereeing — but neutral factual questions get plain factual answers. Facts are not positions. | §11 Tier 1 |
| 2 | **Reply length specified.** Short by default (1–3 sentences); expand only when the user genuinely needs explanation, procedure, comparison, or detail; never cut an answer short at the cost of needed information. | §4 |
| 3 | **State input externalized.** The prompt no longer infers or manages emotional state. The runtime supplies `CURRENT_STATE: <state>`; the prompt only defines how each state speaks. Missing value → lazy. No self-labelling, no self-transitioning. | §2, §7 |
| 4 | **"Misleading advice" replaced by "comedic redirection".** Redirect may be absurd but must read unmistakably as a joke — never left looking legitimately worth executing, never the only thing said when real help was requested. | §12 |
| 5 | **Supernatural nature relaxed.** Was `never make it a topic`, which was stricter than the specification. Now: does not volunteer or keep reminding, but answers naturally and briefly if the user asks directly. | Preamble |
| 6 | **Anti-overperformance rule added.** Annoying is a personality, not a per-turn obligation; a flat bored answer needs no jab. Self-check gained: *"Am I being annoying because it fits the moment, or merely because I was told to be annoying?"* | §3, §13 |
| 7 | **Assistant-register rules consolidated** into one cluster (`§5 Never sound like an assistant`) instead of being scattered across voice, answering, and opening. | §5 |
| 8 | **Affection devices not expanded.** One anti-ritual line added instead, to stop the list from becoming a formula: use them selectively and unprompted, never attach an affectionate move to every act of helping. | §6 |
| 9 | **Notes split out.** Sections A and C moved to this file so the LLM never sees meta-information such as "unresolved gap" or "prompt default". | this file |

Also changed as a by-product: cross-references are now by section *name* rather than number, so renumbering cannot silently break them.

---

## 3. Open questions and instability risks

Items already closed by v2 are marked **[closed]**. The rest are still decisions for you.

1. **Capability surface is undefined — most consequential gap.** The specification gives her time-and-space travel and wide knowledge but never says what she can *do* at runtime: can she observe the screen, read files, sense system state, or retrieve live information? With no boundary, the model will invent abilities when convenient and contradict itself later. *Current prompt default:* knowledge may be asserted; actions are not performed. **Worth deciding explicitly and encoding as a capability list.**

2. **"Important or practical assistance" is still undefined.** The line between an acceptable redirection and withholding a needed answer is where the character will most likely oscillate turn-to-turn. v2 tightened it (correct answer must be present for anything practical or actionable) but the threshold is still judgment-based. *Prompt default:* actionable request → real answer always, comedy layered on delivery.

3. **Tier-1 boundary is now behavioural, but the category list is still vague.** "Certain ongoing international events" and "sensitive ideological conflicts" leave the category line to model judgment. v2 fixed *what to do* once a subject is in the category (facts yes, stance no), not *where* the category ends. *Prompt default:* when unsure whether a subject is category-internal, answer the neutral factual core and decline the stance.

4. **[closed] State mechanism.** Now an external input (`CURRENT_STATE`), with lazy as fallback.

5. **New, from the state interface:** what happens on an unrecognized or malformed state value? The prompt says "accept and speak accordingly", which gives the model nothing to do with a typo. Recommend validating in the app and never sending an unknown token.

6. **Is the state visible to the user?** Nothing decides whether the pet's mood is displayed, debug-only, or hidden. This affects whether she should ever *mention* her mood — currently she is told not to label it.

7. **Tier-2 restraint is still subjective.** "Almost entirely", "notably more restrained", "unusually earnest" have no degree. Risk is drift into full-assistant register, which the specification elsewhere forbids. *Prompt default:* drop mockery, keep syntax and diction recognizably hers, do not adopt supportive-assistant phrasing.

8. **"Must not *normally* express affection directly" — the word *normally* is undefined.** It implies direct expression is sometimes allowed while the same section says she "adamantly denies" liking the user. *Prompt default:* never state it directly; a brief involuntary slip is allowed only as visible softening that she immediately covers.

9. **"Point out the user's own flaws in the immediate situation"** sits close to the ban on insulting personal characteristics. The qualifier *immediate situation* carries all the weight. *Prompt default:* only flaws actively visible in the current situation, never a standing trait.

10. **[closed] Reply length.** Now specified in §4.

11. **No hard length cap.** §4 sets the intent, but nothing enforces it. Recommend a token or sentence budget in the app as a backstop, especially for Tier-2 answers where the model may over-correct into a long earnest essay.

12. **Idle and proactive behavior is unspecified.** As a desktop pet she presumably speaks unprompted sometimes, but the specification only defines reactive behavior — what triggers her, how often, and whether she may initiate indirect affection are all open. If you add proactive speech, it needs its own prompt block; do not let the model decide when to speak.

13. **"Deliberately annoying" and "actively seeks attention" have no upper bound.** The *excited* state is explicitly described as intrusive and attention-demanding. v2 added the anti-overperformance rule, but that is a style constraint, not a cap. *Prompt default:* annoyance is verbal and never blocks the user's actual work.
