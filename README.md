# throughline-gds-service

The **UK Government Digital Service (GDS) Service Standard** — the 14 points a public
service is assessed against — expressed as a
[throughline](https://pypi.org/project/throughline/) **source**: a standalone,
grounded requirements graph that a consuming project composes with
[throughline-compose](https://github.com/timebacksolutions/throughline-compose).

This repository holds no code. It is a directory of small YAML items with permanent
UIDs, validated by `tl check`. Consumers import it under a namespace and reference
its points as `gds:UR-0005` or its assessment expectations as `gds:SR-0021`.

> This is the **Service Standard** (the 14 assessment points), distinct from the
> GOV.UK **Design System** components (a separate source). Don't conflate them.

## Structure

- **Five value-intents** (`INT-0001`…`INT-0005`) as sibling roots, each
  `normative: false` — a "why" layer above the points.
- The **14 points** as `user_requirement`s that each `derives_from` the one value
  they primarily serve (`UR-0001`…`UR-0014`), each carrying its point number in
  `attrs.source_ref` (`"Point 5"`).
- The concrete **assessment expectations** drawn from each point's guidance as
  `system_requirement`s that `implements` their point UR, carrying the same point
  number in `attrs.source_ref`.

### The five value-intents are *our* choice, not the published Standard

The GDS Service Standard publishes its **14 points as a flat list** — it defines no
grouping or "why" layer above them. The five value-intents in `intents/` are **this
source's own modelling decision**: an authored distillation of the distinct purposes
the Standard encodes, added so the graph has a root layer that `tl trace`/`tl blast`
can walk. They are not part of the official Standard and carry no point number; each
one's `attrs.source_ref` is tagged `"GDS Service Standard — <theme>"` to make its
authored, non-canonical status explicit. If you only trust the published text, read
the points (`UR-*`) and expectations (`SR-*`); the intents are our editorial scaffolding.

We deliberately ground each point to a **single** value (single-parent grounding).
Genuine cross-cuts are expressed with non-grounding `relates` links rather than a
second parent, so tracing stays unambiguous. The point-to-value mapping:

| Value-intent | Points |
| --- | --- |
| `INT-0001` Services are led by real user needs | 1, 2 |
| `INT-0002` Everyone can use it and succeed | 3, 4, 5 |
| `INT-0003` Empowered teams keep improving in production | 6, 7, 8 |
| `INT-0004` The service is trustworthy | 9, 14 |
| `INT-0005` Public money spent accountably; services stay open | 10, 11, 12, 13 |

## Modelling conventions

- **throughline UIDs are this source's own** (`UR-0005`, `SR-0021`…), immutable and
  never the point number. The published number lives in `attrs.source_ref`.
- The Service Standard has no formal edition tags, so a single `main` is the line of
  record; a release is tagged (e.g. `v2026-07`) when a pass is considered complete.

## Composing it

In a consuming throughline project's `throughline.toml`:

```toml
[[sources]]
namespace = "gds"
path = "vendor/throughline-gds-service"   # or a pinned checkout
```

Then reference a point or expectation from your own items:

```yaml
links:
- target: gds:UR-0005          # Point 5, make sure everyone can use the service
  type: satisfies
```

`tl-compose check` resolves the reference; bare `tl check` fails fast and points you
at `tl-compose`.

## Local checks

```sh
pip install throughline
tl check --strict     # the graph must stay sound
tl docs --check       # docs/spec.md must match the graph
```

## Provenance

The GDS Service Standard is © Crown copyright, published on GOV.UK under the Open
Government Licence v3.0. See [NOTICE](NOTICE) and
https://www.gov.uk/service-manual/service-standard. This repository is Apache-2.0
for its structure and tooling; the reproduced guidance text remains Crown copyright
under the OGL.
