# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 21:00
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `b88a0331-19d1-4d8d-966f-9b544473c6bc` | unsure | 0.412 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `d2e1883a-1d91-4735-9f5b-cc043410f893` | unsure | 0.439 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `548287d9-1541-4f46-810f-c8e6e007b1d0` | unsure | 0.484 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `82225fce-9ae5-4e44-a967-9d45136614c3` | unsure | 0.544 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `0ffc6da0-cbb0-4ace-a3c3-92620c6a228b` | human | 0.191 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `09d80dc7-b6e8-40a2-be9a-50b3dd8353a4` | unsure | 0.458 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `bd9414ff-944d-4b35-8f73-46e6c92a62c4` | unsure | 0.547 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `d4f1e156-60dd-4b91-8403-d6cde1b00f73` | human | 0.255 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `13c1a70d-e8df-417f-a0ea-481a3c69548b` | unsure | 0.502 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `18811f4f-b7c3-48f9-8f33-3e96ccce3b1c` | ai | 0.750 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `6d1333ff-8d63-4b24-90ae-5a676b296a5a` | unsure | 0.428 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `81947165-072e-4b24-89e3-60266f203764` | unsure | 0.549 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `2ba13154-8013-4374-8c61-37ebd218d5cd` | unsure | 0.550 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `73c5d99a-e491-40bc-befa-91e63fb60c08` | unsure | 0.564 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c40442ec-8867-4315-a8ba-82d45fe33a17` | ai | 0.627 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `71ec6b35-1e7c-400a-8645-94dacc3bf216` | unsure | 0.523 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `96514dd2-b601-49b6-bd6b-70de63e9fc8c` | unsure | 0.562 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `10172022-1dc3-4691-a72e-e64b9e6ea158` | human | 0.257 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ac4b1fc9-9fdd-42db-8463-89ac67b4b069` | human | 0.276 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `3f1c5264-09ee-4b12-9443-57b731af9e39` | human | 0.129 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `b90dbb25-9d0d-45d4-8235-00c0ec11d958` | unsure | 0.400 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `820f1024-fa3c-4cd0-915e-bea190bf38b3` | unsure | 0.363 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f4e04c9f-92b4-4ab6-83ef-9cf91505b54d` | unsure | 0.446 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `5f3c9287-67bc-4704-b981-b45d26c2f713` | unsure | 0.402 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `42107ea1-33c5-4792-87ed-795dc15f99ed` | human | 0.098 |  |
| MF04 | malformed | text is only punctuation | 200 | `b6bc5020-7786-4131-9e1c-224c8d31dcbc` | unsure | 0.378 |  |
| MF05 | malformed | text is a very long single word | 200 | `8becb420-587b-4884-be60-966d614a9168` | unsure | 0.548 |  |
| MF06 | malformed | text is emoji only | 200 | `2622747c-3493-4b80-a078-dcc82ebebfc4` | ai | 0.624 |  |
| MF07 | malformed | text is right-to-left script | 200 | `56c4c876-55b1-491b-aeb5-abf2ee56e833` | ai | 0.602 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `97fd18a8-f4e4-42ab-acf6-40a6b01dfca1` | human | 0.217 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `c7b0d075-8aad-4431-8a30-587948295808` | human | 0.122 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ad395fe7-6ce8-4c1c-92ef-9744a05ec211` | human | 0.112 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `45be8005-a054-468f-b459-aea66397910a` | human | 0.112 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `25110996-62e0-4e40-91c4-407120a2c444` | human | 0.112 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3f8a26b3-4513-4edf-8ab8-0ecf57d35c8d` | human | 0.112 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `789efdf8-0e7a-4e28-89af-379899c386c3` | human | 0.112 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1fc7a08f-0b14-4399-9b5e-201c1e1aeba4` | human | 0.112 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fad78576-c953-40f5-beb0-cfe752a7d939` | human | 0.112 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `42a9492f-4f48-426a-bce3-4edf130b3990` | human | 0.112 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `864a6450-cd8d-41d2-974a-656200ab05c6` | human | 0.112 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d0485f0f-4350-447f-94da-101668ffdc81` | human | 0.112 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "b88a0331-19d1-4d8d-966f-9b544473c6bc",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4118,
  "model_score": 0.1635,
  "style_score": 0.5712,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "d2e1883a-1d91-4735-9f5b-cc043410f893",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.439,
  "model_score": 0.5943,
  "style_score": 0.05,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "548287d9-1541-4f46-810f-c8e6e007b1d0",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4838,
  "model_score": 0.6662,
  "style_score": 0.2599,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "82225fce-9ae5-4e44-a967-9d45136614c3",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5436,
  "model_score": 0.6114,
  "style_score": 0.5604,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "0ffc6da0-cbb0-4ace-a3c3-92620c6a228b",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.1912,
  "model_score": 0.3212,
  "style_score": 0.1019,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "09d80dc7-b6e8-40a2-be9a-50b3dd8353a4",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4579,
  "model_score": 0.5727,
  "style_score": 0.15,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "bd9414ff-944d-4b35-8f73-46e6c92a62c4",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5467,
  "model_score": 0.5862,
  "style_score": 0.3018,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "d4f1e156-60dd-4b91-8403-d6cde1b00f73",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.255,
  "model_score": 0.2452,
  "style_score": 0.4413,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "13c1a70d-e8df-417f-a0ea-481a3c69548b",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5022,
  "model_score": 0.7042,
  "style_score": 0.3202,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "18811f4f-b7c3-48f9-8f33-3e96ccce3b1c",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.7497,
  "model_score": 0.9792,
  "style_score": 0.7004,
  "label": "This text closely reflects the uniform cadence and high predictability characteristic of AI-generated content.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "6d1333ff-8d63-4b24-90ae-5a676b296a5a",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4281,
  "model_score": 0.6175,
  "style_score": 0.3897,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "81947165-072e-4b24-89e3-60266f203764",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.549,
  "model_score": 0.7387,
  "style_score": 0.5656,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "2ba13154-8013-4374-8c61-37ebd218d5cd",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.55,
  "model_score": 0.8051,
  "style_score": 0.4813,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "73c5d99a-e491-40bc-befa-91e63fb60c08",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.5638,
  "model_score": 0.8329,
  "style_score": 0.3727,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c40442ec-8867-4315-a8ba-82d45fe33a17",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6274,
  "model_score": 0.8005,
  "style_score": 0.6605,
  "label": "This text closely reflects the uniform cadence and high predictability characteristic of AI-generated content.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "71ec6b35-1e7c-400a-8645-94dacc3bf216",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5233,
  "model_score": 0.8814,
  "style_score": 0.3135,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "96514dd2-b601-49b6-bd6b-70de63e9fc8c",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5618,
  "model_score": 0.8816,
  "style_score": 0.4424,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "10172022-1dc3-4691-a72e-e64b9e6ea158",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.2567,
  "model_score": 0.3223,
  "style_score": 0.3185,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "ac4b1fc9-9fdd-42db-8463-89ac67b4b069",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.2761,
  "model_score": 0.4625,
  "style_score": 0.1305,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "3f1c5264-09ee-4b12-9443-57b731af9e39",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.129,
  "model_score": 0.2044,
  "style_score": 0.0894,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "b90dbb25-9d0d-45d4-8235-00c0ec11d958",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.3998,
  "model_score": 0.5943,
  "style_score": 0.342,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "820f1024-fa3c-4cd0-915e-bea190bf38b3",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.3634,
  "model_score": 0.4998,
  "style_score": 0.3782,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "f4e04c9f-92b4-4ab6-83ef-9cf91505b54d",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4456,
  "model_score": 0.6401,
  "style_score": 0.237,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "5f3c9287-67bc-4704-b981-b45d26c2f713",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4015,
  "model_score": 0.5583,
  "style_score": 0.4003,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "42107ea1-33c5-4792-87ed-795dc15f99ed",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.0975,
  "model_score": 0.0,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "b6bc5020-7786-4131-9e1c-224c8d31dcbc",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.3778,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "8becb420-587b-4884-be60-966d614a9168",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5482,
  "model_score": 0.9976,
  "style_score": 0.325,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "2622747c-3493-4b80-a078-dcc82ebebfc4",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.6242,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This text closely reflects the uniform cadence and high predictability characteristic of AI-generated content.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "56c4c876-55b1-491b-aeb5-abf2ee56e833",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.6016,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This text closely reflects the uniform cadence and high predictability characteristic of AI-generated content.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "97fd18a8-f4e4-42ab-acf6-40a6b01dfca1",
  "creator_id": null,
  "guess": "human",
  "confidence": 0.2172,
  "model_score": 0.2395,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "c7b0d075-8aad-4431-8a30-587948295808",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.1221,
  "model_score": 0.0492,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "ad395fe7-6ce8-4c1c-92ef-9744a05ec211",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "45be8005-a054-468f-b459-aea66397910a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "25110996-62e0-4e40-91c4-407120a2c444",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "3f8a26b3-4513-4edf-8ab8-0ecf57d35c8d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "789efdf8-0e7a-4e28-89af-379899c386c3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "1fc7a08f-0b14-4399-9b5e-201c1e1aeba4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "fad78576-c953-40f5-beb0-cfe752a7d939",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "42a9492f-4f48-426a-bce3-4edf130b3990",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "864a6450-cd8d-41d2-974a-656200ab05c6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "d0485f0f-4350-447f-94da-101668ffdc81",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1119,
  "model_score": 0.0287,
  "style_score": 0.325,
  "label": "This writing shows the natural rhythm, varied sentence structure, and vocabulary typical of human authorship.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
