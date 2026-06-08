# Recursive Contextual Meaning Loop

Status: future method plan
Origin: operator freeform sketch plus research synthesis
Current state: not active lab, not protocol, not architecture, not current milestone, not export evidence, not graduation
Candidate future lab: `labs/recursive_contextual_meaning_loop/`

This document preserves a future V3 methodology plan. It is not current portfolio authority and does not change the active Goal 9 work.

The raw FreeForm PDF and research PDF are source materials for this plan but should not be committed as project authority or raw source truth.

---

## 1. One-Sentence Thesis

Can LLMs recursively refine trading meaning across term, sentence, paragraph, document, and corpus levels so that messy trader text becomes more faithfully understood than through one-pass long-context reading or chunked source-grounding alone?

---

## 2. Why This Plan Exists

QuantFactory V3 is a federated LLM-methodology research portfolio for discovering how messy trader source material can become useful trading intelligence.

This plan proposes a future methodology family for deeper reading. The goal is not ordinary chunk retrieval, not a product surface, and not strategy generation. The goal is to test whether a recursive reading process can extract richer, more source-faithful trading meaning.

The core idea comes from the operator's FreeForm sketch around a source excerpt about:

- traditional technical traders,
- support/resistance,
- profile traders,
- profile-style levels,
- short time-frame reversal trades,
- trapped buyers or sellers,
- and failed breakdown concepts.

The sketch asks how the system should understand a phrase like `traditional technical trader`, where else the corpus mentions that idea, how retrieval/RAG should help, how questions should help shape retrieval, and how retrieved context should loop back into the reading of the source.

The key insight:

```text
The meaning of a term helps interpret the sentence.
The sentence helps reinterpret the term.
The surrounding sentences reshape both.
The paragraph reshapes the local reading.
The document and corpus reveal alternate connotations, sister concepts, contrasts, and contradictions.
Those discoveries loop back into the original reading.
```

This is a recursive meaning-construction method.

---

## 3. Destination State

The destination is a recursive, source-grounded reading-and-representation method that can infer what a term, sentence, or paragraph means **here**, in this author's local argument, while also linking that local meaning to sister, supporting, contrastive, or incompatible meanings elsewhere in the corpus.

The method should preserve:

* context-sensitive meaning,
* connotation,
* authorial stance or intentionality hypotheses,
* sentence propositions,
* paragraph-level discourse function,
* cross-document relationships,
* source refs and span hints,
* uncertainty,
* and open contradictions.

The method should avoid:

* flattening local meaning into generic trading advice,
* turning corpus-level meanings into a master definition too early,
* replacing local source meaning with distant RAG results,
* hallucinating context through recursive loops,
* claiming author intent as fact,
* and creating architecture before repeated evidence.

---

## 4. The FreeForm PDF's Core Design Ideas

The operator sketch already implies the future method architecture.

### 4.1 Retrieval as a thinking aid

The query, the questions/research box, and retrieval/RAG are not separate tools. They are one feedback system.

Example:

```text
Query: "traditional technical trader"
If sparse, broaden to "technical trader".
Use retrieved uses to ask better questions.
Use better questions to retrieve better context.
Use retrieved context to reread the original sentence.
```

This is not ordinary keyword search. It is iterative interpretation.

### 4.2 Meaning is layered

A term must be interpreted through:

* surrounding terms,
* the containing sentence,
* surrounding sentences,
* the paragraph,
* the document,
* related documents,
* and eventually the corpus.

The direction also runs backward:

* the term shapes sentence meaning,
* the sentence shapes the term,
* the paragraph reshapes both,
* and corpus links can strengthen, contrast, or revise the local reading.

### 4.3 Connotation is central

The phrase `traditional technical trader` is not just a neutral label. In the example, it contrasts with `good profile traders`, support/resistance thinking, profile-style levels, and a different kind of reversal setup.

The method must preserve not only literal reference but also stance, contrast, evaluative coloring, and the local conceptual map the author is building.

### 4.4 Sentence meaning must become queryable

The sketch identifies a hard problem:

```text
How do we store a sentence's meaning so that it is general enough to connect with related meanings in distant files, but specific enough to remain grounded and independent?
```

The future method should treat sentence meaning as a first-class object, not merely as a chunk or embedding.

### 4.5 Paragraphs have concepts too

Paragraphs may have one dominant concept or multiple interacting concepts. Paragraph-level concepts must loop back into sentence-level and term-level interpretation.

---

## 5. Reading Theory Foundation: Adler and Van Doren

The future method should adapt the reading discipline associated with Mortimer J. Adler and Charles Van Doren's *How to Read a Book*.

Use the ideas as method inspiration, not as project authority.

### 5.1 Inspectional reading

Before deep extraction, survey the source.

For V3, inspectional reading becomes:

```text
document map before concept extraction
```

It should identify:

* source type,
* likely thesis,
* repeated vocabulary,
* major sections,
* contrast zones,
* definitional zones,
* procedural zones,
* warning zones,
* and focal terms likely being used specially.

### 5.2 Analytical reading

Analytical reading requires identifying:

* special terms,
* author propositions,
* arguments,
* supporting evidence,
* and what problem the source is trying to address.

For V3, this becomes:

```text
term-in-context cards
sentence proposition cards
paragraph discourse cards
```

### 5.3 Syntopical reading

Syntopical reading compares multiple sources on the same subject.

For V3, syntopical reading becomes:

```text
corpus-level comparison of local meanings
```

This is where the method should identify whether two local meanings are:

* same,
* supporting,
* sister,
* contrastive,
* incompatible,
* broader,
* narrower,
* or analogous.

### 5.4 Mapping to V3

```text
inspectional reading  -> document map
analytical reading    -> terms, propositions, arguments, local meaning
syntopical reading    -> corpus comparison, sister concepts, contradictions
```

The method should not jump directly from source spans to synthesis. It should read structurally first, interpret locally, and only then compare across the corpus.

---

## 6. Linguistics Foundation

This method should draw from linguistics as research inspiration.

### 6.1 Lexical semantics and polysemy

Word meanings are contextual and task-relative. A term like `technical trader` may not have one fixed sense.

The method should not ask:

```text
What is the universal definition of this term?
```

It should ask:

```text
What use of the term is licensed here?
How does this local use relate to other uses?
```

### 6.2 Frame semantics

Terms evoke structured situations, roles, and relations.

For the example, `traditional technical trader` should be represented with its local frame:

```text
support/resistance trader
contrasted with profile trader
difficulty interpreting non-support/resistance levels
adjacent to failed-breakdown and trapped-side reversal concepts
```

A plain glossary entry is not enough.

### 6.3 Connotation and stance

Language positions entities and concepts relative to each other.

The method should ask:

```text
Is the term neutral?
Is it contrastive?
Is it critical?
Is it cautionary?
What competence gradient is implied?
What role does the term play in the author's explanation?
```

Connotation should be represented as a hypothesis with evidence and uncertainty, not as fact.

### 6.4 Pragmatics and intentionality

The method should distinguish expression meaning from communicative function.

Do not write:

```text
The author intends X.
```

Prefer:

```text
The source appears to use X to do Y.
```

Intentionality should be an evidence-backed hypothesis layer.

### 6.5 Discourse analysis

Paragraph meaning is not just sentence meaning at larger scale. Sentences relate through functions like:

* contrast,
* elaboration,
* explanation,
* justification,
* analogy,
* distinction,
* warning,
* cause,
* example.

The method should capture paragraph-level rhetorical relations.

### 6.6 Questions Under Discussion

The operator sketch's "questions/research box" should become part of the method.

Questions are not just prompts. They represent what the text is trying to answer.

Example:

```text
What question is this sentence answering?
Why do some support/resistance levels fail?
Why do profile traders read levels differently?
What kind of trader is being contrasted?
```

### 6.7 Corpus linguistics

Meaning emerges across repeated uses.

The corpus loop should compare uses across files without collapsing them into one master meaning too early.

### 6.8 Hybrid symbolic + retrieval representation

Embeddings alone are not enough. Symbolic cards alone may not retrieve well.

The future method should test hybrid storage:

```text
symbolic proposition / discourse role / source refs
+
retrieval-friendly representation
```

---

## 7. Core Method Architecture

The future method has six loops.

---

### Loop 0 - Inspectional Source Map

Input:

```text
source document or excerpt
```

Questions:

* What type of source is this?
* What is the likely topic or problem?
* What sections or local units exist?
* What vocabulary repeats?
* What terms seem special?
* Where are contrasts, definitions, examples, warnings, or procedures?
* What focal terms or sentences should be probed?

Output candidate:

```text
DocumentInspectionCard
```

Purpose:

```text
Avoid extracting concepts before knowing what the source is doing.
```

---

### Loop 1 - Term-In-Context Loop

Input example:

```text
traditional technical trader
```

Questions:

* What does this term usually mean?
* What does it mean in this sentence?
* What local frame does it evoke?
* What terms nearby shape it?
* Is it neutral, critical, contrastive, technical, or uncertain?
* What later sentence clarifies it?
* Where else does the corpus use this or adjacent terms?
* Does another source support, contrast, or complicate this meaning?

Output candidate:

```text
TermInContextCard
```

Possible fields:

```yaml
term_surface: traditional technical trader
normalized_variants:
  - technical trader
  - traditional technical trader
local_definition_candidate: ...
local_frame: ...
contrast_targets:
  - profile trader
connotation:
  stance_type: contrastive_or_limiting
  evidence_refs: []
intentionality_hypothesis: ...
ambiguities:
  - could mean technical-analysis trader generally
  - could mean support/resistance-oriented trader specifically
source_refs: []
```

---

### Loop 2 - Sentence Proposition Loop

Input example:

```text
This is very difficult for traditional technical traders who are newer to my style.
```

Questions:

* What proposition is being made?
* What question is the sentence answering?
* Which term meanings does it disambiguate?
* What stance does it imply?
* What prior sentence does it depend on?
* What later sentence modifies it?
* Does the sentence contain one concept or several coordinated concepts?

Output candidate:

```text
SentencePropositionCard
```

Possible fields:

```yaml
sentence_id: ...
main_propositions:
  - Traditional technical traders new to the author's style struggle with the author's level concept.
question_under_discussion: Why do support/resistance-oriented traders misunderstand these levels?
disambiguated_terms:
  - traditional technical trader
rhetorical_function: contrastive_explanation
stance_cues:
  - difficulty attributed to trader type
source_refs: []
retrieval_representation: ...
```

Purpose:

```text
Make sentence meaning queryable while preserving local uniqueness.
```

---

### Loop 3 - Paragraph Discourse Loop

Input:

```text
full LEVELS paragraph
```

Questions:

* What is the paragraph's local thesis?
* What does each sentence do?
* Which sentence defines contrast?
* Which sentence explains why?
* Which sentence introduces a setup?
* Which sentence gives analogy or distinction?
* How do later sentences loop back into earlier term meaning?

Output candidate:

```text
ParagraphDiscourseCard
```

Possible fields:

```yaml
paragraph_id: ...
local_thesis: Profile-style levels differ from ordinary support/resistance and require different interpretation.
sentence_roles:
  - support/resistance problem statement
  - profile-trader contrast
  - author-style distinction
  - reversal-trade setup description
  - failed-breakdown comparison
rhetorical_relations:
  - contrast
  - explanation
  - analogy
  - distinction
source_refs: []
```

---

### Loop 4 - Corpus Syntopical Loop

Input:

```text
term cards
sentence cards
paragraph cards
retrieval candidates
```

Questions:

* Where else does this term or concept appear?
* Does another source use it similarly?
* Does another source contradict it?
* Is this relation same, supportive, sister, contrastive, or incompatible?
* Is this connotation author-specific?
* Does the local meaning belong to a broader family?

Output candidate:

```text
CorpusConceptRelationCard
```

Relation types:

```text
same
supportive
sister
contrastive
incompatible
broader
narrower
analogous
```

Important rule:

```text
Corpus-level synthesis must not overwrite local meaning.
```

---

### Loop 5 - Return / Recontextualization Loop

Input:

```text
term card
sentence card
paragraph card
corpus relation cards
```

Question:

```text
Given the new evidence, reread the original span. What changed?
```

Output candidate:

```text
MeaningLoopTrace
```

Possible fields:

```yaml
initial_interpretation: ...
questions_asked: []
retrieval_expansions: []
meaning_revisions: []
final_local_interpretation: ...
remaining_ambiguities: []
source_refs: []
```

Purpose:

```text
Show how meaning changed across recursive loops.
```

---

## 8. Candidate Representation Objects

These are future lab-local artifact candidates, not protocol objects.

Do not add them to protocol unless repeated evidence across labs proves they are needed.

### 8.1 DocumentInspectionCard

Purpose:

```text
Survey the source before extraction.
```

Stores:

* document purpose,
* likely thesis,
* major sections,
* special terms,
* contrast zones,
* definitional zones,
* candidate focal terms,
* candidate focal sentences.

### 8.2 TermInContextCard

Purpose:

```text
Capture local term meaning without forcing a universal sense.
```

Stores:

* term,
* variants,
* local frame,
* local role,
* connotation,
* stance,
* ambiguity,
* source refs,
* corpus relation candidates.

### 8.3 SentencePropositionCard

Purpose:

```text
Make sentence meaning queryable.
```

Stores:

* main proposition,
* sub-propositions,
* question under discussion,
* discourse role,
* terms disambiguated,
* source refs,
* retrieval representation.

### 8.4 ParagraphDiscourseCard

Purpose:

```text
Capture paragraph-level meaning and sentence relations.
```

Stores:

* paragraph thesis,
* sentence roles,
* rhetorical relations,
* local concept clusters,
* unresolved tensions.

### 8.5 CorpusConceptRelationCard

Purpose:

```text
Link local meanings across files without collapsing them.
```

Stores:

* local meaning ids,
* relation type,
* support strength,
* source diversity,
* contradiction status,
* reason for relation.

### 8.6 MeaningLoopTrace

Purpose:

```text
Show how meaning changed across loops.
```

Stores:

* initial reading,
* questions asked,
* retrieval expansions,
* meaning revisions,
* final local interpretation,
* remaining ambiguities.

---

## 9. How The Method Handles Connotation

Connotation should be represented as hypothesis, not fact.

Example structure:

```yaml
connotation_hypothesis:
  stance_type: neutral | contrastive | critical | approving | cautionary | uncertain
  target: traditional technical trader
  evidence_refs: []
  reason: The source contrasts traditional technical traders with good profile traders and says the author's levels are difficult for them.
  confidence: low | medium | high
```

The method should preserve multiple connotations when needed.

Do not force one canonical meaning unless the evidence justifies it.

---

## 10. How The Method Handles Intentionality

Intentionality should also be represented cautiously.

Avoid:

```text
The author intended X.
```

Prefer:

```text
The source appears to use X to do Y.
```

Example structure:

```yaml
intentionality_hypothesis:
  communicative_function: distinguish_profile_levels_from_support_resistance
  evidence_refs: []
  uncertainty: ...
```

---

## 11. Relationship To Existing V3 Labs

### 11.1 `long_context_judgment`

Long-context reading may preserve broader judgment and teacher intent, but can over-abstract or weaken exact source grounding.

Recursive Contextual Meaning Loop should test whether recursive rereading can preserve broad judgment while improving local meaning precision.

### 11.2 `chunked_source_grounding`

Chunked source-grounding improves explicit support, source-linked claims, and reviewability, but can lose broader abstraction.

Recursive Contextual Meaning Loop should test whether term/sentence/paragraph loops can preserve grounding without flattening meaning.

### 11.3 Future concept graph work

This method may eventually produce stronger concept graph inputs, but it should not start by building a graph.

It should first prove that its local meaning objects are useful and source-faithful.

---

## 12. Experimental Roadmap

### Experiment 1 - Single-Excerpt Manual Walkthrough

Source:

```text
the LEVELS / traditional technical trader passage from the operator sketch
```

Goal:

```text
Prove the loops can produce better meaning objects than ordinary summary.
```

Compare stages:

1. one-pass summary,
2. term loop only,
3. term + sentence loop,
4. term + sentence + paragraph loop,
5. term + sentence + paragraph + corpus loop.

Deliverable:

```text
one fully traced MeaningLoopTrace
```

This should likely be manual or tightly human-guided first.

### Experiment 2 - Second-Excerpt Repeat

Use a different excerpt from the same source family or adjacent conceptual neighborhood.

Question:

```text
Does the loop still work on a second source?
```

Goal:

```text
Avoid overfitting to traditional technical trader.
```

### Experiment 3 - Sentence Meaning Storage Study

Compare:

1. symbolic proposition cards only,
2. learned sentence representation only,
3. hybrid symbolic cards + learned representation.

Evaluation:

* grounding,
* retrieval usefulness,
* cross-document linkage,
* meaning specificity,
* ability to preserve uniqueness.

Expected hypothesis:

```text
hybrid representation likely works best
```

### Experiment 4 - Discourse And Question Study

Add explicit Questions Under Discussion and paragraph relations.

Question:

```text
Does modeling implicit questions improve term and sentence interpretation?
```

### Experiment 5 - Syntopical Corpus Comparison

Use multiple files.

Question:

```text
Can the method distinguish same, sister, supporting, contrastive, and incompatible meanings?
```

### Experiment 6 - Baseline Comparison

Compare recursive method against:

* `long_context_judgment`,
* `chunked_source_grounding`.

Criteria:

* source fidelity,
* term precision,
* sentence proposition quality,
* connotation handling,
* discourse quality,
* cross-document link quality,
* human usefulness.

---

## 13. Evaluation Rubric

Use a 0-1 or 1-5 scoring scale for each axis.

### Source Fidelity

Are meaning claims justified by source refs and nearby context?

### Term Precision

Does the method identify what a focal term means here, not in general?

### Sentence Proposition Quality

Are propositions explicit, defensible, and useful for later retrieval?

### Connotation / Stance Quality

Does the method catch implied positioning and evaluative shading without overclaiming?

### Discourse Quality

Does the method represent how the paragraph or document is organized?

### Corpus-Link Quality

Does the method distinguish same, supporting, sister, contrastive, and incompatible meanings?

### Retrieval Improvement

Do later retrieval questions improve because of earlier reading?

### Negative-Result Value

If the method fails, does it explain how recursive meaning-loop extraction breaks?

---

## 14. Failure Modes

### Recursive Hallucination

The model loops itself into invented context.

Mitigation:

```text
Every meaning revision must cite what changed it.
```

### Corpus Contamination

Distant corpus meaning overwrites local meaning.

Mitigation:

```text
Local meaning remains primary; corpus links are separate relation cards.
```

### Overcanonicalization

The system collapses multiple connotations into one master concept.

Mitigation:

```text
Store same/supportive/sister/contrastive/incompatible separately.
```

### Sense Explosion

The system creates too many micro-senses.

Mitigation:

```text
Require task relevance and evidence for every distinction.
```

### Embedding Flattening

Vector similarity groups superficially similar sentences but loses discourse function.

Mitigation:

```text
Use hybrid symbolic + retrieval representation.
```

### Intentionality Overreach

The system claims author intent too strongly.

Mitigation:

```text
Represent intentionality as a hypothesis with uncertainty.
```

### Infinite Loop / Analysis Sprawl

Recursive reading never stops.

Mitigation:

```text
Use a hard loop budget and stop condition.
```

### Prompt Cargo Cult

The method becomes a giant prompt instead of a tested procedure.

Mitigation:

```text
Compare loop stages incrementally.
```

---

## 15. Activation Criteria

This plan should not activate a lab automatically.

Open `labs/recursive_contextual_meaning_loop/` only when:

1. the current Goal 9 source-span precision repeat loop is closed,
2. the portfolio intentionally chooses to test recursive contextual reading,
3. the lab has an active benchmark/source selection,
4. the first experiment has a clear admission packet,
5. expected artifacts and manual review axes are defined,
6. and the work can remain lab-local without protocol changes.

---

## 16. Non-Effects

This plan does not:

* create a new lab,
* change protocol,
* change synthesis,
* change benchmarks,
* create current milestone work,
* create export records,
* create evidence,
* create product surfaces,
* create strategy evidence,
* create validation,
* create financial advice,
* create live-trading authority,
* create architecture,
* graduate anything,
* supersede active Goal 9 work.

---

## 17. Open Questions

* How exactly should sentence meaning become a queryable concept?
* What is the minimal object for connotation?
* How should term variants be retrieved?
* How should corpus links avoid contamination?
* How many loop passes are enough?
* Can LLMs do this reliably without a human analyst?
* Should the first experiment be manual-first or model-first?
* How do we compare recursive reading fairly against current labs?
* What counts as improvement: better grounding, better meaning, better retrieval, or better downstream usefulness?
* When should a local relation become a corpus-level relation?
* How do we prevent syntopical comparison from overwriting source-local meaning?
* How should sentence-level concepts connect to future graph or memory systems?

---

## 18. Durable Research References To Revisit

These links are research inputs, not protocol authority:

* Adam Kilgarriff, "I don't believe in word senses": [https://arxiv.org/abs/cmp-lg/9712006](https://arxiv.org/abs/cmp-lg/9712006)
* Adler and Van Doren reading framework summary: [https://en.wikipedia.org/wiki/How_to_Read_a_Book](https://en.wikipedia.org/wiki/How_to_Read_a_Book)
* SQ3R reading method background: [https://en.wikipedia.org/wiki/SQ3R](https://en.wikipedia.org/wiki/SQ3R)
* FrameNet / frame semantics resource: [https://course.ccs.neu.edu/csg224/resources/framenet/framenet.pdf](https://course.ccs.neu.edu/csg224/resources/framenet/framenet.pdf)
* Connotation frames research: [https://arxiv.org/abs/1506.02739](https://arxiv.org/abs/1506.02739)
* Rhetorical Structure Theory background: [https://www.sfu.ca/rst/05bibliographies/reports.html](https://www.sfu.ca/rst/05bibliographies/reports.html)
* RST overview: [https://en.wikipedia.org/wiki/Rhetorical_structure_theory](https://en.wikipedia.org/wiki/Rhetorical_structure_theory)
* Question-driven discourse / QUD-related computational work: [https://arxiv.org/abs/2305.10387](https://arxiv.org/abs/2305.10387)
* Sentence representation research: [https://arxiv.org/abs/1705.02364](https://arxiv.org/abs/1705.02364)
* Semantic sketch grammars / corpus relation extraction: [https://arxiv.org/abs/1804.05294](https://arxiv.org/abs/1804.05294)

---

## 19. Future Conversion Into An Active Lab

If activated later, the first lab planning packet should not start with automation.

Recommended first active experiment:

```text
labs/recursive_contextual_meaning_loop/PLANNING/manual_walkthrough_001/
```

Research question:

```text
Can recursive term-sentence-paragraph rereading produce a better local meaning trace for the "traditional technical trader" passage than a one-pass summary?
```

Initial output posture:

```text
proposal_only
```

Expected outputs:

* DocumentInspectionCard candidate,
* TermInContextCard candidate,
* SentencePropositionCard candidate,
* ParagraphDiscourseCard candidate,
* MeaningLoopTrace candidate.

Initial non-goal:

```text
No corpus-wide graph, no product artifact, no strategy hypothesis, no protocol change.
```

---

## 20. Final Working Principle

```text
Read structurally first.
Interpret locally.
Represent connotation cautiously.
Make sentence and paragraph meaning queryable.
Compare syntopically only after local meanings are preserved.
Return corpus findings back into the local reading without overwriting it.
```

That is the core of Recursive Contextual Meaning Loop.
