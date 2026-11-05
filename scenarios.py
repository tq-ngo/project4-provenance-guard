"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it.
- Criterion 1 (False positive rate on human writing): 10 pieces of verified human writing.
- Criterion 2 (Score spread between canonical AI and human text): 5 AI passages and 5 human passages.
- Criterion 3 (Label reachability across all three tiers): Inputs spanning human, unsure, and AI bands.
- Criterion 4 (Deterministic appeal recording and state transition): 5 submissions appealed with reasoning.
- Criterion 5 (Graceful rejection of malformed inputs): 5 malformed and boundary test payloads.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            # 1. Technical debugging reflection
            "I spent four hours yesterday tracking down a phantom bug in my cache invalidation code. "
            "It only happened when three users clicked update at the exact same millisecond, and even then "
            "only on Redis cluster nodes running in production. Classic race condition. I ended up adding "
            "distributed locks around the write sequence, but honestly, distributed systems never fail to "
            "humble me when I least expect it.",

            # 2. Local environment setup
            "Setting up a new dev machine is always a bittersweet ritual. On one hand, you get a pristine, "
            "clutter-free terminal and instant build times. On the other, you realize you forgot half your "
            "custom zsh aliases, your SSH keys aren't authorized for half the repositories, and your git "
            "commit signing key is sitting on a thumb drive in another drawer.",

            # 3. Distributed systems lecture notes
            "In lecture today we covered the Raft consensus algorithm and compared it to Multi-Paxos. "
            "Raft makes leader election and log replication much easier to understand by breaking them into "
            "explicit, isolated subproblems. The professor emphasized how randomized election timeouts "
            "prevent split votes in practice, which was a neat practical trick compared to abstract theory.",

            # 4. Family cooking memory
            "Whenever my grandmother makes pho on Sunday mornings, the whole house smells like charred ginger "
            "and star anise before seven o'clock. She simmers the beef bones for at least twelve hours, skimming "
            "the surface every half hour with a small wire spoon. No shortcuts, no bouillon cubes—just patience, "
            "rock sugar, and good fish sauce.",

            # 5. Local coffee shop review
            "The coffee shop on the corner has great espresso and terrible acoustics. Concrete floors, bare brick "
            "walls, and high exposed ceilings turn every clinking plate and steamed milk wand into an echoing roar. "
            "If you want to read a book in peace, bring noise-canceling headphones; otherwise, you'll hear the entire "
            "story of someone's startup pitch from three tables away.",

            # 6. Database migration reflection
            "Migrating our legacy Postgres tables to MongoDB during my summer internship taught me a lot about "
            "data modeling tradeoffs. We thought ditching relational foreign keys would speed up our queries, "
            "but we ended up writing dozens of manual consistency checks in application code instead. Turns out "
            "the database engine was doing that work much better than we were.",

            # 7. Open-source economics reflection
            "Reading about the maintainer burnout in critical open-source libraries was pretty sobering. Millions "
            "of profitable companies rely on tiny packages maintained by one person in their spare time on a weekend. "
            "Until corporate sponsorship models become routine and dependable, we're basically building internet "
            "infrastructure on top of unpaid volunteer goodwill.",

            # 8. Garage bicycle repair
            "I finally replaced the frayed rear brake cable and rusty chain on my ten-speed bike this afternoon. "
            "Tuning the indexing on the rear derailleur took three attempts because the barrel adjuster was seized, "
            "but once I sprayed some penetrating oil and adjusted the limit screws, the gears clicked smoothly into "
            "place on the test ride down our hill.",

            # 9. Semester balance reflection
            "Balancing four engineering courses with thirty hours of research and trying to cook dinner every night "
            "feels like juggling bowling balls on a unicycle. Some weeks you feel on top of everything; other weeks "
            "you live on instant ramen and cold brew while finishing a problem set at two in the morning.",

            # 10. TypeScript vs JavaScript reflection
            "I used to think TypeScript was unnecessary boilerplate for small projects, but after refactoring a "
            "ten-thousand line web app, I will never go back. Being able to change a function signature and have "
            "the compiler highlight every single broken callsite in milliseconds saves entire afternoons of runtime "
            "debugging.",
        ],
    },
    {
        "name": "score spread canonical AI vs human",
        "criterion": 2,
        "texts": [
            # 5 Canonical AI texts (formulaic, uniform, high transition markers)
            "The implementation of sustainable energy systems represents a pivotal challenge in modern environmental "
            "policy. Furthermore, accelerating the global transition toward renewable power sources requires "
            "substantial investment in grid infrastructure and grid-scale storage solutions. Additionally, "
            "policymakers must establish equitable incentives that encourage broad technological adoption while "
            "safeguarding vulnerable communities. In conclusion, interdisciplinary collaboration remains crucial "
            "for achieving long-term environmental sustainability and resilient economic growth.",

            "Artificial intelligence models have demonstrated notable advancements across diverse scientific domains. "
            "Moreover, integrating machine learning algorithms into clinical workflows enhances diagnostic precision "
            "and streamlines patient care protocols. Furthermore, rigorous validation frameworks must be established "
            "to guarantee data privacy and mitigate algorithmic bias throughout model deployment. In summary, the "
            "responsible adoption of computational methodologies is imperative for ensuring safe clinical outcomes.",

            "Effective project management requires a comprehensive understanding of organizational objectives and team "
            "capabilities. Additionally, maintaining structured communication protocols enables distributed teams to "
            "coordinate their daily responsibilities with minimal operational friction. Furthermore, documenting key "
            "deliverables throughout each development cycle ensures transparent accountability and mitigates potential "
            "project risks. In conclusion, consistent oversight remains fundamental to delivering quality results.",

            "Urban transportation systems are undergoing significant transformations driven by technological innovation. "
            "Furthermore, expanding public transit networks and integrating multimodal mobility options reduces "
            "metropolitan traffic congestion and lowers carbon emissions. Additionally, data-driven traffic management "
            "enhances operational efficiency and improves overall commuter safety. In summary, sustained municipal "
            "investment is essential for building resilient, future-ready urban infrastructure.",

            "The integration of digital educational tools has reshaped instructional strategies in modern classrooms. "
            "Moreover, utilizing adaptive learning platforms enables educators to tailor curriculum pathways to meet "
            "individual student competencies. Furthermore, providing equitable access to digital resources ensures "
            "that all learners benefit from enhanced technological opportunities. In conclusion, pedagogical "
            "innovation plays a decisive role in fostering student engagement and academic excellence.",

            # 5 Canonical Human texts (varied sentence lengths, idioms, conversational texture)
            "Wait, what just happened? I stared at the terminal output for five straight minutes, completely bewildered. "
            "The server was supposed to restart cleanly after the maintenance window. Instead, every worker process died "
            "with an out-of-memory signal. Sixty gigabytes gone in seconds. Turns out a misplaced comma in our config file "
            "caused an infinite retry loop that spammed the connection pool until the operating system gave up.",

            "The rain finally stopped around dusk, leaving a thick mist hanging over the salt marsh. We walked down "
            "to the dock in rubber boots, listening to the creak of wet mooring lines and the low hum of a distant tugboat. "
            "The air smelled sharp—mud, brine, and old creosote. We didn't talk much on the way back, just watched the "
            "lighthouse beam sweep across the gray channel every ten seconds.",

            "Look, nobody actually enjoys writing regex. You write something that looks like line noise, test it on three "
            "strings, convince yourself it works, and push to production. Three days later a user submits an email address "
            "with a plus sign and the entire signup form crashes with a catastrophic backtracking error. Tale as old as time.",

            "My cat has exactly two modes: completely comatose on the living room rug, or sprinting down the hallway at "
            "three in the morning at supersonic speed chasing a moth that might not even exist. There is no middle ground. "
            "None. Just absolute tranquility followed by violent parkour off the kitchen refrigerator.",

            "I found an old notebook from my first year of college while cleaning out my closet. Pages upon pages of "
            "handwritten calculus equations, doodles of spaceships in the margins, and coffee stains on every third leaf. "
            "I could barely read my own handwriting from four years ago, but the sheer panic before the midterms was still "
            "vividly recorded in the frantic exclamation points.",
        ],
    },
    {
        "name": "label reachability",
        "criterion": 3,
        "texts": [
            # 2 Human candidates (organic cadence, varied syntax -> target high-confidence human)
            "Honestly? I had zero expectations going into that workshop. My advisor basically pushed me out the door "
            "and told me to network. But the speaker on distributed tracing was incredible—he spent half the time showing "
            "spectacular production disasters and explaining exactly why their monitoring failed. Hilarious, practical, "
            "and shockingly honest.",

            "We packed the car at sunrise, threw our sleeping bags in the trunk, and hit the highway before traffic hit. "
            "The diner on Route 9 served blueberry pancakes the size of hubcaps with hot black coffee. You could see the "
            "fog lifting off the river valley through the greasy diner window.",

            # 2 Borderline candidates (clear academic/informational text -> target unsure)
            "The protocol relies on periodic heartbeat messages to verify node availability across the cluster. "
            "When a follower node fails to receive a heartbeat within the configured timeout interval, it transitions "
            "to the candidate state and initiates an election sequence. Other nodes evaluate the candidate's log index "
            "before casting their ballots.",

            "Photosynthesis converts solar energy into chemical bonds within plant cells. Chlorophyll molecules inside the "
            "chloroplasts absorb photons primarily in the blue and red wavelengths, initiating the light-dependent reactions "
            "that synthesize ATP and NADPH for subsequent sugar production in the Calvin cycle.",

            # 2 AI candidates (formulaic transitions, uniform structure -> target high-confidence AI)
            "Technological advancements in cloud computing have revolutionized modern enterprise architecture. "
            "Furthermore, adopting microservices patterns allows organizations to scale individual functional components "
            "independently while reducing overall maintenance overhead. Additionally, automated deployment pipelines "
            "streamline software delivery cycles and minimize human error. In conclusion, strategic cloud migration "
            "drives competitive advantage and operational resilience.",

            "Digital literacy represents an essential competency in today's knowledge-based economic landscape. "
            "Moreover, educational institutions must incorporate comprehensive digital skills curricula to prepare "
            "students for technological careers. Furthermore, fostering equitable technological access ensures inclusive "
            "opportunities across all demographic sectors. In summary, proactive digital education remains vital for "
            "future workforce readiness.",
        ],
    },
    {
        "name": "appeal recording and transition",
        "criterion": 4,
        "bodies": [
            {
                "action": "appeal",
                "text": "This methodology section outlines our experimental benchmark configurations for the compiler evaluation.",
                "creator_id": "eval_appeal_01",
                "reasoning": "I drafted this methodology myself using standard compiler literature. The formal tone reflects academic conventions.",
            },
            {
                "action": "appeal",
                "text": "The distributed storage cluster utilizes consistent hashing to partition key-value pairs evenly across available server nodes.",
                "creator_id": "eval_appeal_02",
                "reasoning": "This is my own systems coursework submission. The terminology is technical because the topic requires precise specifications.",
            },
            {
                "action": "appeal",
                "text": "The literature review examines renewable energy policy initiatives across European municipal governments over the past decade.",
                "creator_id": "eval_appeal_03",
                "reasoning": "English is my second language, so I write deliberately with structured transition words. That does not make it machine generated.",
            },
            {
                "action": "appeal",
                "text": "Our experimental results demonstrate significant latency reductions when caching hot relational queries in memory.",
                "creator_id": "eval_appeal_04",
                "reasoning": "Original research writeup with experimental metrics. The phrasing is concise and direct by design.",
            },
            {
                "action": "appeal",
                "text": "The proposed application architecture separates presentation concerns from business validation logic through modular service boundaries.",
                "creator_id": "eval_appeal_05",
                "reasoning": "I wrote this architectural summary for my team's design review. All explanations are authentic human work.",
            },
        ],
    },
    {
        "name": "bad input handling",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 987654, "creator_id": "eval_bad_number"},
            {"text": "overflow " * 10000, "creator_id": "eval_bad_oversize"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
