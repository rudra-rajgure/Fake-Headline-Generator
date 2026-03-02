from flask import Flask, render_template, request
import random

app = Flask(__name__)

data = {

    "gaming": {
        "subjects": [
            "A GTA VI fan waiting since 2013",
            "A guy who said 'last match' at 11 PM",
            "A hostel gamer with 2% battery",
            "A PUBG pro using hotel WiFi"
        ],
        "actions": [
            "rage quits after",
            "blames teammates for",
            "starts motivational speech after",
            "throws controller seeing"
        ],
        "things": [
            "999 ms ping",
            "server maintenance notice",
            "mom switching off WiFi",
            "a teammate playing on speaker mode"
        ]
    },

    "politics": {
        "subjects": [
            "An uncle watching news at full volume",
            "A WhatsApp University graduate",
            "Two TV debate experts shouting",
            "A politician before elections"
        ],
        "actions": [
            "promises free WiFi after seeing",
            "starts emotional speech about",
            "blames previous government for",
            "holds emergency meeting over"
        ],
        "things": [
            "a viral meme",
            "petrol price discussion",
            "a confusing policy nobody read",
            "a trending Twitter fight"
        ]
    },

    "internet": {
        "subjects": [
            "An Instagram reels addict",
            "A sigma motivation page admin",
            "A guy posting 'no one supports me'",
            "An influencer with ring light at 3 AM"
        ],
        "actions": [
            "goes viral after posting",
            "gets cancelled for",
            "uploads apology video about",
            "starts podcast discussing"
        ],
        "things": [
            "a cringe reel",
            "fake hustle advice",
            "a mysterious crypto scheme",
            "a comment section war"
        ]
    },

    "student": {
        "subjects": [
            "An engineering student one night before exam",
            "A topper saying 'I didn't study'",
            "A backbencher opening syllabus for first time",
            "A group project leader doing everything alone"
        ],
        "actions": [
            "panic studies for",
            "realizes syllabus includes",
            "cries peacefully over",
            "searches YouTube for"
        ],
        "things": [
            "5 units in 2 hours",
            "an assignment due tomorrow",
            "PDF notes from unknown senior",
            "a 2x speed lecture"
        ]
    },

    "tech": {
        "subjects": [
            "A programmer after fixing one bug",
            "A coder copying from StackOverflow",
            "An AI chatbot giving confidence",
            "A startup founder with only ideas"
        ],
        "actions": [
            "accidentally creates",
            "deploys causing",
            "celebrates before discovering",
            "blames laptop for"
        ],
        "things": [
            "17 new errors",
            "production server crash",
            "'works on my machine' problem",
            "an error nobody understands"
        ]
    }
}


def generate_headline(category):
    # fallback if wrong category
    if category not in data:
        category = random.choice(list(data.keys()))

    g = data[category]

    headline = (
        f"BREAKING NEWS: "
        f"{random.choice(g['subjects'])} "
        f"{random.choice(g['actions'])} "
        f"{random.choice(g['things'])}"
    )

    return headline


@app.route("/")
def home():
    category = request.args.get("category", "gaming")
    headline = generate_headline(category)
    return render_template("index.html", headline=headline)


if __name__ == "__main__":
    app.run(debug=True)