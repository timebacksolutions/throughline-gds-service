#!/usr/bin/env python3
"""Generate the throughline item files for the GDS Service Standard source.

Faithfully re-expresses the 14 points of the UK Government Digital Service (GDS)
Service Standard (https://www.gov.uk/service-manual/service-standard) as a grounded
IDD graph:

    INT-0001  (root intent, why the Service Standard exists; normative: false)
      -> UR-0001..UR-0014   one user_requirement per point (derives_from intent)
           -> SR-000N        assessment expectations (implements the point UR)

UIDs are this source's own and immutable; the published point number lives in
attrs.source_ref. Content is Crown copyright, reproduced under the Open Government
Licence v3.0. Run from the repo root: `python tools/generate_from_gds.py`.

Using a generator (rather than hand-writing YAML) keeps every value going through
the YAML dumper, sidestepping throughline's colon-space plain-scalar trap.
"""
from __future__ import annotations

import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

INTENT = dict(
    uid="INT-0001",
    title="Public services meet real user needs and are good enough to be trusted",
    text=(
        "The GDS Service Standard exists so that public services are built around "
        "real user needs, are simple and accessible for everyone, and are delivered "
        "and run well enough to be trusted — giving teams a shared, assessable "
        "baseline for what a good public service looks like rather than ad-hoc "
        "judgement."
    ),
    source_ref="GDS Service Standard",
)

# Each point: (title, expectation text, [assessment expectation SR texts])
POINTS = [
    (
        "Understand users and their needs",
        "Develop a deep understanding of users and the problem the service is trying "
        "to solve for them, looking at the whole context of what users are trying to "
        "achieve and not just their interaction with government.",
        [
            "Conduct user research to understand user needs, supplemented by "
            "secondary research and analysis where applicable.",
            "Create quick, throwaway prototypes to test the team's hypotheses about "
            "users and the problem.",
            "Use web analytics and other available data (such as call-centre data or "
            "third-party services) to deepen understanding of the problem.",
        ],
    ),
    (
        "Solve a whole problem for users",
        "Work towards a service that solves a whole problem for users, designed "
        "around their needs rather than around technologies or pre-selected "
        "solutions, working with other teams and organisations where necessary.",
        [
            "Understand any genuine constraints affecting the service (for example "
            "legislative constraints) and work with policy professionals to solve the "
            "problems those constraints cause.",
            "Scope the service according to how users think and what they need to do "
            "— neither too narrow nor too broad.",
            "Check whether the problem has already been solved and reuse existing "
            "solutions where possible.",
            "Be able to explain how the service joins up with other things into a "
            "journey that solves a whole problem for users.",
            "Take responsibility for agreeing how the user journey works with the "
            "organisations responsible for its different parts.",
            "Consider alternatives to building a service, such as publishing content, "
            "running a campaign, partnering, or making data or an API available.",
            "Work in the open so people inside and outside the organisation know what "
            "the team is doing.",
            "Minimise the number of times users have to provide the same information "
            "to government, while respecting their privacy.",
        ],
    ),
    (
        "Provide a joined-up experience across all channels",
        "Work towards a service that meets users' needs across all the channels they "
        "need, which could be a mix of online, phone, paper and face to face.",
        [
            "Give the service team the authority to identify the best solutions "
            "across channels.",
            "Involve front-line operations and policy staff in user research and "
            "prioritisation, with designers collaborating with operations on the "
            "user experience.",
            "Be able to test and change both digital and non-digital channels, "
            "coordinating online changes with their offline impacts.",
            "Ensure operations staff understand the digital service and are kept "
            "updated, and that promoting digital take-up does not obscure other "
            "access channels.",
        ],
    ),
    (
        "Make the service simple to use",
        "Build a service that is simple, intuitive and comprehensible, and test it "
        "with users to make sure it works for them.",
        [
            "Help the user do the thing they need to do as simply as possible, so "
            "people succeed first time with the minimum of help.",
            "Test for usability frequently with actual and potential users, using "
            "appropriate research techniques.",
            "Test all the parts of the service the user interacts with — online parts "
            "and offline parts such as letters.",
            "Design the service to work online across the range of devices that "
            "reflects users' behaviour.",
        ],
    ),
    (
        "Make sure everyone can use the service",
        "Provide a service that everyone can use, including disabled people and "
        "people with other legally protected characteristics, and people who do not "
        "have access to the internet or lack the skills or confidence to use it.",
        [
            "Meet accessibility standards for both the online and offline parts of "
            "the service.",
            "Avoid excluding any groups within the audience the service is intended "
            "to serve.",
            "Carry out research with participants who represent the potential "
            "audience, including people with access needs.",
            "Provide appropriate assisted digital support so people are not excluded "
            "for lack of digital skills or internet access.",
        ],
    ),
    (
        "Have a multidisciplinary team",
        "Put together a multidisciplinary team with a diverse mix of skills and "
        "expertise, including the people involved in decision making, so the team is "
        "accountable and can respond quickly to what it learns about users.",
        [
            "Build the service with a multidisciplinary team appropriate to the "
            "current phase, co-located as much as possible, with decision-makers "
            "accountable to the team.",
            "Include expertise in how the service is delivered across the relevant "
            "offline channels and the back-end systems it must integrate with.",
            "Give the team access to the specialist expertise it needs (for example "
            "legal, policy or industry-specific analysis).",
            "Where the team works with contractors and outside suppliers, do so on a "
            "sustainable basis.",
        ],
    ),
    (
        "Use agile ways of working",
        "Use agile methods to get the service in front of real users as soon as "
        "possible, observing how they use it and iterating based on what is learned, "
        "reducing the risk of delivering the wrong thing.",
        [
            "Work in an agile way — inspecting, learning and adapting as the team "
            "goes.",
            "Use governance arrangements consistent with the agile governance "
            "principles, keeping the right people informed at the right level of "
            "detail.",
            "Where appropriate and proportionate, test the service with the minister "
            "or relevant senior stakeholder.",
        ],
    ),
    (
        "Iterate and improve frequently",
        "Make sure the service has the capacity, resources and technical flexibility "
        "to iterate and improve frequently — not just in early development but "
        "throughout the life of the service.",
        [
            "Retain the capacity, resources and technical flexibility to make "
            "substantial improvements throughout the life of the service, not only "
            "in its early phases.",
        ],
    ),
    (
        "Create a secure service which protects users' privacy",
        "Understand how to manage risks throughout the delivery lifecycle and put "
        "robust security measures in place to protect against potential threats "
        "while respecting users' privacy.",
        [
            "Follow the Secure by Design principles across the delivery lifecycle.",
            "Make senior leaders who are accountable for security aware of the risks.",
            "Have a plan and budget to manage security across the life of the "
            "service, including responding to new threats and changed requirements.",
            "Perform due diligence on the security of third-party software.",
            "Do user research to create security processes that are fit for purpose "
            "and easy to understand.",
            "Collect, process and store data securely and in a way that respects "
            "users' privacy.",
            "Maintain an assessment of security risks and mitigate threats with "
            "appropriate protections, working with business and information risk "
            "teams.",
            "Anticipate and manage vulnerabilities and regularly test security "
            "controls.",
        ],
    ),
    (
        "Define what success looks like and publish performance data",
        "Work out what success looks like for the service and identify metrics that "
        "show what is working and what can be improved, combined with user research.",
        [
            "Identify metrics that show how well the service solves its intended "
            "problem and track performance against them.",
            "Use performance data to decide what to fix and how to improve the "
            "service.",
            "For central government services, publish data on the mandatory key "
            "performance indicators.",
        ],
    ),
    (
        "Choose the right tools and technology",
        "Choose tools and technology that let the team create a high-quality service "
        "in a cost-effective way, minimising the cost of changing direction in "
        "future.",
        [
            "Choose tools and technology that let the team build and operate a "
            "high-quality service cost-effectively, using automation where feasible.",
            "Make and be able to justify sound build-versus-buy decisions, using "
            "common platforms where suitable.",
            "Understand how the chosen technology works, including emerging "
            "technologies and artificial intelligence.",
            "Consider the total cost of ownership and keep the freedom to change "
            "direction later, for example by using open standards to avoid vendor "
            "lock-in.",
            "Have an effective strategy for managing any legacy technology the "
            "service depends on or integrates with.",
            "Assess how technology choices affect user experience and accessibility, "
            "and avoid choices that compromise the reliability of information or the "
            "quality of decisions.",
        ],
    ),
    (
        "Make new source code open",
        "Because public services are built with public money, make the source code "
        "open and reusable unless there is a good reason not to — avoiding vendor "
        "lock-in and enabling reuse across government.",
        [
            "Write code in the open from the start and publish it in open "
            "repositories, excluding sensitive information such as credentials and "
            "secret keys.",
            "Retain ownership of the intellectual property for new source code and "
            "license it for reuse.",
            "Recognise the limited exceptions (such as code tied to an unannounced "
            "government policy) where code should not be published.",
        ],
    ),
    (
        "Use and contribute to open standards, common components and patterns",
        "Build on open standards and common components and patterns from inside and "
        "outside government, and contribute back what the team creates.",
        [
            "Use open standards, and propose a new open standard where none already "
            "meets the need.",
            "Use standard government technology components where possible.",
            "Maximise flexibility in the use of technology, for example by using and "
            "creating APIs and, where possible, authoritative sources of data.",
            "Use common components and patterns and share any new ones created or "
            "adapted, for example by contributing to the GOV.UK Design System.",
        ],
    ),
    (
        "Operate a reliable service",
        "Minimise service downtime and have a plan to deal with it when it does "
        "happen, so the service is dependable for the people who rely on it.",
        [
            "Maximise the uptime and responsiveness of the online part of the "
            "service.",
            "Deploy software changes frequently without significant downtime.",
            "Carry out regular quality-assurance testing overseen by the service "
            "team, not by automated tools alone.",
            "Test the service in an environment that matches live conditions.",
            "Put proportionate, sustainable monitoring and incident response in "
            "place.",
            "Monitor user outcomes and ethical issues such as bias, not only "
            "technical faults.",
            "Work actively to resolve organisational or contractual barriers to "
            "availability.",
        ],
    ),
]


def _dump(path: pathlib.Path, item: "dict[str, object]") -> None:
    with path.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(
            item,
            fh,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=88,
        )


def main() -> None:
    # Root intent.
    intent = dict(
        uid=INTENT["uid"],
        type="intent",
        status="approved",
        title=INTENT["title"],
        text=INTENT["text"],
        normative=False,
        attrs=dict(source_ref=INTENT["source_ref"]),
    )
    _dump(ROOT / "intents" / f"{INTENT['uid']}.yml", intent)

    sr_n = 0
    for idx, (title, text, criteria) in enumerate(POINTS, start=1):
        ur_uid = f"UR-{idx:04d}"
        point_ref = f"Point {idx}"
        ur = dict(
            uid=ur_uid,
            type="user_requirement",
            status="approved",
            title=title,
            text=text,
            links=[dict(target=INTENT["uid"], type="derives_from")],
            attrs=dict(source_ref=point_ref),
        )
        _dump(ROOT / "points" / f"{ur_uid}.yml", ur)

        for crit in criteria:
            sr_n += 1
            sr_uid = f"SR-{sr_n:04d}"
            # Title: a short, testable label derived from the criterion's first clause.
            short = crit.rstrip(".")
            if len(short) > 70:
                short = short[:67].rstrip() + "..."
            sr = dict(
                uid=sr_uid,
                type="system_requirement",
                status="approved",
                title=short,
                text=crit,
                links=[dict(target=ur_uid, type="implements")],
                attrs=dict(source_ref=point_ref),
            )
            _dump(ROOT / "requirements" / f"{sr_uid}.yml", sr)

    _write_spec()

    print(f"wrote INT-0001, 14 point URs, {sr_n} assessment SRs, docs/spec.md skeleton")


def _write_spec() -> None:
    """Write docs/spec.md with `tl:*` markers. `tl docs` injects the graph content
    into the marked regions; the prose headings here are hand-owned. Every item must
    appear in a published doc or `tl check --strict` fails the `unpublished` rule."""
    lines: list[str] = []
    lines.append("# GDS Service Standard — throughline source\n")
    lines.append(
        "This document is **generated from the graph** by `tl docs`; `tl docs "
        "--check` gates\nit in CI. The prose headings are hand-owned — everything "
        "between `tl:*` markers is\ninjected from the YAML items, so the published "
        "spec can never drift from the graph.\n"
    )
    lines.append(
        "This source expresses the **UK Government Digital Service (GDS) Service "
        "Standard**:\nits "
        "<!-- tl:count type == 'user_requirement' -->\n0\n<!-- tl:end --> points, "
        "each a `user_requirement`, and\n"
        "<!-- tl:count type == 'system_requirement' -->\n0\n<!-- tl:end --> "
        "assessment expectations, each a `system_requirement` that `implements` its\n"
        "point. The published point number lives in `attrs.source_ref` (e.g. "
        "`Point 5`); the\nthroughline UIDs are this source's own and immutable — a "
        "consumer cites a point as\n`gds:UR-0005`, never by its point number.\n"
    )
    lines.append("## Purpose\n")
    lines.append(
        "<!-- tl:item INT-0001 -->\n<!-- tl:end -->\n"
    )
    for idx, (title, _text, _criteria) in enumerate(POINTS, start=1):
        ur_uid = f"UR-{idx:04d}"
        point_ref = f"Point {idx}"
        lines.append(f"## {point_ref}. {title}\n")
        lines.append(f"<!-- tl:item {ur_uid} -->\n<!-- tl:end -->\n")
        lines.append(
            "<!-- tl:table type == 'system_requirement' and "
            f"attrs.get('source_ref') == '{point_ref}' -->\n<!-- tl:end -->\n"
        )
    (ROOT / "docs" / "spec.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
