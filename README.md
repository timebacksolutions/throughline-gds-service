# standard-gds-service

The **UK Government Digital Service (GDS) Service Standard** — the 14 points a public
service is assessed against — expressed as a
[throughline](https://pypi.org/project/throughline/) **source**: a standalone,
grounded requirements graph that a consuming project composes with
[throughline-compose](https://github.com/rhodium-org/throughline-compose).

This repository holds no code. It is a directory of small YAML items with permanent
UIDs, validated by `tl check`. Consumers import it under a namespace and reference
its points as `gds:UR-0005` or its assessment expectations as `gds:SR-0021`.

> This is the **Service Standard** (the 14 assessment points), distinct from the
> GOV.UK **Design System** components (a separate source). Don't conflate them.

## Structure

- `INT-0001` — the root intent (why the Service Standard exists), `normative: false`.
- The **14 points** as `user_requirement`s that `derives_from` the intent
  (`UR-0001`…`UR-0014`), each carrying its point number in `attrs.source_ref`
  (`"Point 5"`).
- The concrete **assessment expectations** drawn from each point's guidance as
  `system_requirement`s that `implements` their point UR, carrying the same point
  number in `attrs.source_ref`.

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
path = "vendor/standard-gds-service"   # or a pinned checkout
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
