"""
LinkedIn Post Generator for krmaazha
Run this to generate a fresh post with rotated hashtags.
Usage: python post_generator.py [template_number] [--hashtags N]
Example: python post_generator.py 1 --hashtags 8
"""
import sys
import random
import argparse

TEMPLATES = {
    1: {
        "name": "The Hook / Educational",
        "post": """I reviewed {num_resumes} resumes last month.

{fail_percent}% failed the ATS screen before a human ever opened them.

Not because the candidates were unqualified. Because their resumes were built for humans, not machines.

Here is what I learned:

1. Keyword stuffing does not work. ATS looks for semantic relevance, not word count.
2. PDF formatting breaks parser logic. Some systems read left-to-right, others top-to-bottom. A two-column resume can become alphabet soup.
3. "Results-driven" and "spearheaded" are red flags. Hiring managers scan for AI cliches and downgrade those resumes.

I built a 5-agent AI system that fixes all three:
- Agent 1 maps the job post for exact skill requirements and tone
- Agent 2 matches your real experience against those gaps
- Agent 3 writes in natural sentences (no bullets, no hyphens, no AI tell-signs)
- Agent 4 formats for your target region (USA, UK, EU, Middle East, APAC)
- Agent 5 composes a personalized outreach message that references the actual job post

The result? Resumes that pass ATS and sound like you wrote them.

If you want to see what is broken in your resume, send it to krmaazha@gmail.com and book a $5 review call. I will audit it live and show you exactly what the 5-agent system would fix."""
    },
    2: {
        "name": "The Contrarian Take",
        "post": """ChatGPT can not tailor your resume properly.

It writes the same generic output for everyone. It uses banned phrases hiring managers downvote. It does not read the actual job post you are applying to. It does not know if you are applying in Germany (needs photo) versus the US (never photo).

What actually works:
- A system that reads the job post FIRST
- A profile matcher that maps your real skills to the role requirements
- Anti-AI writing rules so the output sounds human
- Region-specific formatting

That is what I built. 5 agents. Real tailoring. Not a template swap.

$5 resume review. krmaazha@gmail.com. No sales pitch. Just a real audit."""
    },
    3: {
        "name": "The Story / Social Proof",
        "post": """"I sent {num_resumes} resumes and got {callbacks} callbacks."

That is what a client told me before we worked together.

After running their resume through the 5-agent system for {roles} targeted roles, they got {interviews} interviews in {weeks} weeks.

The difference was not their experience. It was relevance.

Their original resume listed everything they had ever done. The tailored versions connected their exact skills to each job post, using the language from the posting itself.

Hiring managers do not care what you CAN do. They care what you can do FOR THEM.

If your resume is a generalist document, you are invisible.

Fix it: krmaazha@gmail.com | $5 review call"""
    },
    4: {
        "name": "The Quick Value Post",
        "post": """3 signs your resume is failing ATS:

1. You use a two-column template. ATS parsers read linearly. Columns scramble your content.
2. You have a "Skills" section with 30 buzzwords. ATS looks for contextual usage, not lists.
3. You apply with the same resume to every role. ATS scores relevance. Generic = low score.

Fix = tailored resume per role. Not copy-paste. Real mapping.

I built a system that does this in minutes. $5 review to see what is broken in yours.

krmaazha@gmail.com"""
    },
    5: {
        "name": "The Personal Story / Authority",
        "post": """I spent {years} years in data engineering and AI. I watched smart people get rejected by software before a person ever judged them.

So I built something to fix it.

A 5-agent AI pipeline that:
- Reads job posts like a recruiter
- Maps your skills against the real requirements
- Writes in your voice, not AI-speak
- Formats for your target country

It is not a template. It is not ChatGPT with a new prompt. It is a system.

If you are tired of sending resumes into black holes, send yours to krmaazha@gmail.com. $5 gets you a real audit. No pitch."""
    }
}

HASHTAGS_PRIMARY = ["#JobSearch", "#ResumeTips", "#CareerAdvice", "#ATS", "#Hiring", "#TechJobs"]
HASHTAGS_NICHE = ["#DataScience", "#MachineLearning", "#AI", "#SoftwareEngineering", "#ProductManagement", "#UXDesign", "#TechHiring", "#RemoteWork"]
HASHTAGS_ENGAGEMENT = ["#LinkedInTips", "#JobHunting", "#InterviewPrep", "#CareerGrowth", "#ProfessionalDevelopment", "#JobSearch2026"]
HASHTAGS_BRANDED = ["#ResumeReview", "#TailoredResume", "#BeatTheATS", "#JobApplication", "#CareerChange"]

def get_hashtags(count=8):
    """Generate a random but balanced set of hashtags."""
    primary = random.sample(HASHTAGS_PRIMARY, min(2, len(HASHTAGS_PRIMARY)))
    niche = random.sample(HASHTAGS_NICHE, min(2, len(HASHTAGS_NICHE)))
    engagement = random.sample(HASHTAGS_ENGAGEMENT, min(1, len(HASHTAGS_ENGAGEMENT)))
    branded = random.sample(HASHTAGS_BRANDED, min(1, len(HASHTAGS_BRANDED)))
    
    all_tags = primary + niche + engagement + branded
    random.shuffle(all_tags)
    return " ".join(all_tags[:count])

def generate_post(template_num, hashtag_count=8):
    if template_num not in TEMPLATES:
        print(f"Error: Template {template_num} not found. Choose from: {list(TEMPLATES.keys())}")
        sys.exit(1)
    
    template = TEMPLATES[template_num]
    post = template["post"]
    
    # Fill in dynamic variables based on template
    if template_num == 1:
        post = post.format(
            num_resumes=random.choice([47, 52, 38, 61, 44]),
            fail_percent=random.choice([73, 68, 71, 75, 66])
        )
    elif template_num == 3:
        post = post.format(
            num_resumes=random.choice([200, 150, 180, 220]),
            callbacks=random.choice([3, 2, 4, 1]),
            roles=random.choice([5, 3, 7, 4]),
            interviews=random.choice([4, 3, 5, 6]),
            weeks=random.choice([2, 3, 1])
        )
    elif template_num == 5:
        post = post.format(years=random.choice([5, 6, 7, 4]))
    
    hashtags = get_hashtags(hashtag_count)
    
    print(f"\n{'='*60}")
    print(f"  TEMPLATE: {template['name']}")
    print(f"{'='*60}\n")
    print(post)
    print(f"\n{hashtags}")
    print(f"\n{'='*60}")
    print(f"  POST LENGTH: {len(post + hashtags)} characters")
    print(f"  (LinkedIn limit: 3,000 characters)")
    print(f"{'='*60}\n")
    
    # Save to file
    filename = f"generated_post_{template_num}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(post + "\n\n" + hashtags)
    print(f"Saved to: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Generate LinkedIn posts for krmaazha")
    parser.add_argument("template", type=int, nargs="?", default=1, help="Template number (1-5)")
    parser.add_argument("--hashtags", type=int, default=8, help="Number of hashtags (default: 8)")
    parser.add_argument("--list", action="store_true", help="List all templates")
    
    args = parser.parse_args()
    
    if args.list:
        print("\nAvailable templates:")
        for num, template in TEMPLATES.items():
            print(f"  {num}. {template['name']}")
        return
    
    generate_post(args.template, args.hashtags)

if __name__ == "__main__":
    main()
