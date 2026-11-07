# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-06 19:56
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `89774d10-1dd6-4a2c-bdff-9faafe1ac8d8` | unsure | 0.412 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `bdbb5feb-d485-4081-b17f-bce0347ca7c1` | unsure | 0.439 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `ca491e44-e2e4-46a1-9608-ab89f7b8643c` | unsure | 0.484 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `47004e2e-dc92-4b78-a79e-853dc9e18de2` | unsure | 0.544 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `87699f4c-d650-4de2-ada5-044999d484b7` | human | 0.191 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `283999b9-d45c-40c8-b51b-feb833b17644` | unsure | 0.458 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `53093385-f5ec-4134-b5ee-895144f81c50` | unsure | 0.547 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `223cfa7e-183f-413f-a16e-bbde30083be5` | human | 0.255 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `f27c92c4-a06e-48f9-8824-9533522f0716` | unsure | 0.502 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `3ae73b3a-1174-4910-a0fa-3008f99e8d94` | ai | 0.750 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `7aae336e-04b5-4eb7-a45f-5f3c9245b4bd` | unsure | 0.428 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `915c4202-5aae-4631-9c9f-73652004e4fe` | unsure | 0.549 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `288950fd-7c50-405e-bc59-147263615ccc` | unsure | 0.550 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `1d1d3de9-98c4-4b5b-bb42-c91f07ec8a46` | unsure | 0.564 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `e363a28b-5209-4225-83b2-34c99fd912a5` | unsure | 0.627 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `74f83ba0-7687-4a73-8789-e6cf4d8ef9a7` | unsure | 0.523 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `983b864f-cde3-4b1f-a767-cfbb7891197b` | unsure | 0.562 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `cc4abf1e-9794-496d-a732-1763cd07d177` | human | 0.257 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `bf3f5cf0-efd6-4654-af3c-edccbae19e18` | human | 0.276 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `97dabdf6-65c8-43be-a309-8ecb091c0b2b` | human | 0.129 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `423c1c37-3719-4bf1-9d03-67c5dbffa6d2` | unsure | 0.400 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `23877324-37fc-4301-a6d9-c4127bd07121` | unsure | 0.363 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `3970d4e5-2ee5-4183-8dee-4075a823c3f6` | unsure | 0.446 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `7e2c04a6-5fd5-4399-9679-5cd6dd48af13` | unsure | 0.402 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `c481ca8c-3c4f-4d48-bae1-869182726cea` | unsure | 0.602 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `cdf6bdd2-f429-43ab-a83a-4c5a50f5b577` | human | 0.217 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `f9c530f2-c51a-4059-9a0e-d0779ade1d23` | human | 0.122 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `da8fc490-ea7a-4c56-a221-947ec814e4fa` | human | 0.112 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `19e5a468-0a1f-4c08-8ca9-d186d26ffa3d` | human | 0.112 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a583f7d8-c57a-4d31-ae4b-6352c7099b0e` | human | 0.112 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `259e531b-931d-42ae-9b76-d4301399f026` | human | 0.112 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `79016dbd-7fcd-4e13-880a-226bf01c0b94` | human | 0.112 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4aaa042f-8def-4327-a5fb-cac4303ccb6d` | human | 0.112 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d2f11ed-f20d-4f09-90ba-e14ae66252a0` | human | 0.112 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `851d59e4-d65b-437c-8eb6-95d095824005` | human | 0.112 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b547138f-bd02-43e4-97d0-6cc09a1fc98f` | human | 0.112 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1c853474-6f2c-4239-b58c-b12479d6e37e` | human | 0.112 |  |
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
  "content_id": "89774d10-1dd6-4a2c-bdff-9faafe1ac8d8",
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
  "content_id": "bdbb5feb-d485-4081-b17f-bce0347ca7c1",
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
  "content_id": "ca491e44-e2e4-46a1-9608-ab89f7b8643c",
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
  "content_id": "47004e2e-dc92-4b78-a79e-853dc9e18de2",
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
  "content_id": "87699f4c-d650-4de2-ada5-044999d484b7",
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
  "content_id": "283999b9-d45c-40c8-b51b-feb833b17644",
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
  "content_id": "53093385-f5ec-4134-b5ee-895144f81c50",
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
  "content_id": "223cfa7e-183f-413f-a16e-bbde30083be5",
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
  "content_id": "f27c92c4-a06e-48f9-8824-9533522f0716",
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
  "content_id": "3ae73b3a-1174-4910-a0fa-3008f99e8d94",
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
  "content_id": "7aae336e-04b5-4eb7-a45f-5f3c9245b4bd",
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
  "content_id": "915c4202-5aae-4631-9c9f-73652004e4fe",
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
  "content_id": "288950fd-7c50-405e-bc59-147263615ccc",
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
  "content_id": "1d1d3de9-98c4-4b5b-bb42-c91f07ec8a46",
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
  "content_id": "e363a28b-5209-4225-83b2-34c99fd912a5",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6274,
  "model_score": 0.8005,
  "style_score": 0.6605,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
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
  "content_id": "74f83ba0-7687-4a73-8789-e6cf4d8ef9a7",
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
  "content_id": "983b864f-cde3-4b1f-a767-cfbb7891197b",
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
  "content_id": "cc4abf1e-9794-496d-a732-1763cd07d177",
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
  "content_id": "bf3f5cf0-efd6-4654-af3c-edccbae19e18",
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
  "content_id": "97dabdf6-65c8-43be-a309-8ecb091c0b2b",
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
  "content_id": "423c1c37-3719-4bf1-9d03-67c5dbffa6d2",
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
  "content_id": "23877324-37fc-4301-a6d9-c4127bd07121",
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
  "content_id": "3970d4e5-2ee5-4183-8dee-4075a823c3f6",
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
  "content_id": "7e2c04a6-5fd5-4399-9679-5cd6dd48af13",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "c481ca8c-3c4f-4d48-bae1-869182726cea",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6016,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We couldn't determine the origin of this text with confidence; it contains a blend of predictable patterns and stylistic variation.",
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
  "content_id": "cdf6bdd2-f429-43ab-a83a-4c5a50f5b577",
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
  "content_id": "f9c530f2-c51a-4059-9a0e-d0779ade1d23",
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
  "content_id": "da8fc490-ea7a-4c56-a221-947ec814e4fa",
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
  "content_id": "19e5a468-0a1f-4c08-8ca9-d186d26ffa3d",
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
  "content_id": "a583f7d8-c57a-4d31-ae4b-6352c7099b0e",
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
  "content_id": "259e531b-931d-42ae-9b76-d4301399f026",
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
  "content_id": "79016dbd-7fcd-4e13-880a-226bf01c0b94",
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
  "content_id": "4aaa042f-8def-4327-a5fb-cac4303ccb6d",
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
  "content_id": "7d2f11ed-f20d-4f09-90ba-e14ae66252a0",
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
  "content_id": "851d59e4-d65b-437c-8eb6-95d095824005",
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
  "content_id": "b547138f-bd02-43e4-97d0-6cc09a1fc98f",
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
  "content_id": "1c853474-6f2c-4239-b58c-b12479d6e37e",
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
