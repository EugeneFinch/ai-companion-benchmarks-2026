# AI Companion & Virtual Girlfriend Benchmarks (2026)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dataset Version](https://img.shields.io/badge/Dataset-2026.10-blue.svg)](data/benchmarks-2026.json)
[![Platforms Audited](https://img.shields.io/badge/Platforms%20Audited-16-green.svg)](data/benchmarks-2026.csv)
[![Audited by](https://img.shields.io/badge/Audited%20by-CrushCritic-ff2d6f.svg)](https://crushcritic.com)

An empirical benchmark dataset and consumer testing audit evaluating **16 leading AI companion and virtual girlfriend platforms**. Testing was conducted firsthand over 250+ hours of conversational interaction, measuring long-term memory retention, filter censorship, multimedia generation latency, privacy policies, and recurring subscription economics (Updated September 30, 2026).

Maintained by the editorial research lab at **[CrushCritic](https://crushcritic.com)**.

---

## 📊 Executive Summary & Key Findings (2026)

1. **Memory Decay is the #1 Failure Point:** 68% of companion apps experience significant conversational drift after just 20 dialogue turns. Only top-tier platforms (**[Candy AI](https://crushcritic.com/candy-ai-review-2026-features-pricing-honest-verdict/)**, **[Kindroid](https://crushcritic.com/kindroid-review/)**, and **[Nomi AI](https://crushcritic.com/nomi-ai-review/)**) maintain structured memory journals or vector recall beyond 7 days of inactivity.
2. **The Censorship Split:** Mainstream mobile applications (Character.AI, Replika, Talkie) enforce strict content moderation filters. Adult and unrestricted roleplay has shifted entirely to specialized web platforms like **[Candy AI](https://crushcritic.com/candy-ai-review-2026-features-pricing-honest-verdict/)**, **[Kupid AI](https://crushcritic.com/kupid-ai-review/)**, and **[SpicyChat](https://crushcritic.com/spicychat-review/)**.
3. **Data Privacy Deficits:** Out of 16 audited platforms, **62% train their models on private user messages** or fail to publish concrete account deletion timelines. Always check the [Data Safety Audit](#-data-safety--privacy-audit) before sharing sensitive personal details.

---

## 🏆 Master Benchmark Leaderboard

| Rank | Platform | Overall Score | Context Memory | NSFW / Roleplay | Voice Calls | Monthly Price | Annual Rate | Full Lab Audit |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **#1** | **[Candy AI](https://crushcritic.com/candy-ai-review-2026-features-pricing-honest-verdict/)** | **9.6 / 10** | 9.2 | Fully Uncensored (Zero Filter) | Yes (Low-latency) | $13.99/mo | $3.99/mo | [Review &rarr;](https://crushcritic.com/candy-ai-review-2026-features-pricing-honest-verdict/) |
| **#2** | **[Kupid AI](https://crushcritic.com/kupid-ai-review/)** | **9.2 / 10** | 8.8 | Fully Uncensored | Yes (Custom Voice) | $14.99/mo | $7.49/mo | [Review &rarr;](https://crushcritic.com/kupid-ai-review/) |
| **#3** | **[Kindroid](https://crushcritic.com/kindroid-review/)** | **9.0 / 10** | 9.8 | Uncensored Roleplay | Yes (High-Fidelity) | $13.99/mo | $9.99/mo | [Review &rarr;](https://crushcritic.com/kindroid-review/) |
| **#4** | **[Nomi AI](https://crushcritic.com/nomi-ai-review/)** | **8.9 / 10** | 9.5 | Uncensored Roleplay | Yes (Voice Mode) | $15.99/mo | $8.33/mo | [Review &rarr;](https://crushcritic.com/nomi-ai-review/) |
| **#5** | **[DreamGF](https://crushcritic.com/dreamgf-review/)** | **8.7 / 10** | 8.0 | Fully Uncensored | Audio playback | $19.99/mo | $9.99/mo | [Review &rarr;](https://crushcritic.com/dreamgf-review/) |
| **#6** | **[Muah AI](https://crushcritic.com/muah-ai-review/)** | **8.5 / 10** | 8.2 | Fully Uncensored | Real-time calls | $14.99/mo | $9.99/mo | [Review &rarr;](https://crushcritic.com/muah-ai-review/) |
| **#7** | **[Character.AI](https://crushcritic.com/character-ai-review/)** | **8.3 / 10** | 8.5 | Filtered (PG-13) | Voice streaming | $9.99/mo | $9.99/mo | [Review &rarr;](https://crushcritic.com/character-ai-review/) |
| **#8** | **[Replika](https://crushcritic.com/replika-review/)** | **8.1 / 10** | 8.0 | Moderate Filter | 3D Voice Calls | $19.99/mo | $5.83/mo | [Review &rarr;](https://crushcritic.com/replika-review/) |
| **#9** | **[SpicyChat](https://crushcritic.com/spicychat-review/)** | **8.0 / 10** | 7.6 | Fully Uncensored | TTS Preview | $14.95/mo | $12.50/mo | [Review &rarr;](https://crushcritic.com/spicychat-review/) |
| **#10** | **[Crushon.ai](https://crushcritic.com/crushon-ai-review/)** | **7.9 / 10** | 7.5 | Toggleable Filter | TTS Audio | $14.90/mo | $9.90/mo | [Review &rarr;](https://crushcritic.com/crushon-ai-review/) |
| **#11** | **[GirlfriendGPT](https://crushcritic.com/girlfriendgpt-review/)** | **7.8 / 10** | 7.2 | Fully Uncensored | Audio Clips | $14.99/mo | $9.99/mo | [Review &rarr;](https://crushcritic.com/girlfriendgpt-review/) |
| **#12** | **Janitor AI** | **7.7 / 10** | 7.8 | Fully Uncensored | None | Free / API | Free | [Compare &rarr;](https://crushcritic.com/compare/) |
| **#13** | **Chub AI** | **7.6 / 10** | 8.4 | Fully Uncensored | None | $5.00/mo | $50.00/yr | [Compare &rarr;](https://crushcritic.com/compare/) |
| **#14** | **Talkie AI** | **7.4 / 10** | 6.8 | Filtered (Store Compliant)| Voice Cards | $9.99/mo | $5.99/mo | [Compare &rarr;](https://crushcritic.com/compare/) |
| **#15** | **PolyBuzz** | **7.2 / 10** | 6.5 | Moderate Filter | None | $9.99/mo | $7.99/mo | [Compare &rarr;](https://crushcritic.com/compare/) |
| **#16** | **Linky** | **7.0 / 10** | 6.4 | Filtered (App Store Compliant)| Audio Clips | $11.99/mo | $7.50/mo | [Compare &rarr;](https://crushcritic.com/compare/) |

*For dynamic side-by-side spec filters, see the live [CrushCritic Interactive Matrix](https://crushcritic.com/compare/), the [18+ Uncensored AI Girlfriends Directory](https://crushcritic.com/porn/), the head-to-head [Candy AI vs Nomi AI Showdown (2026)](https://crushcritic.com/candy-ai-vs-nomi-ai/), or [Full 2026 Rankings](https://crushcritic.com/rankings/).*

### 📖 Laboratory Prompt & Studio Guides (September 2026)
* **[Candy AI Prompts & Chat Requests Master Guide (50+ Tested Prompts)](https://crushcritic.com/candy-ai-prompts-and-chat-requests-guide/)**: In-depth roleplay scenarios, persona calibration, and token usage optimization.
* **[How to Request Custom Photos & Voice Notes on Candy AI](https://crushcritic.com/how-to-request-photos-and-voice-notes-on-candy-ai/)**: Technical mechanics of triggering realistic multimedia and audio notes without prompt degradation.
* **[Candy AI "Direct Her" Mode Prompts Cheat Sheet](https://crushcritic.com/candy-ai-direct-her-mode-prompts-cheat-sheet/)**: Tested lens settings, camera angles, lighting conditions, and dynamic poses.
* **[Candy AI Character Creator Studio Guide](https://crushcritic.com/candy-ai-character-creator-studio-guide/)**: Building customized photorealistic and anime waifu models from prompt seeds.

---

## 🔒 Data Safety & Privacy Audit

Privacy policies were manually audited against explicit clauses regarding model training, advertising sharing, and deletion turnaround:

| Platform | Trains on Private Messages? | Shares with Advertisers? | Account Deletion Window | Security Audit |
| :--- | :---: | :---: | :---: | :---: |
| **Candy AI** | Yes | Aggregated / Service Partners | 30 days | Verified SSL / PCI-DSS |
| **Kupid AI** | **No** | **No** | **Immediate** | High Privacy Grade |
| **Kindroid** | **No (Isolated Tenant)** | **No** | 7 days | High Privacy Grade |
| **Nomi AI** | **No** | **No** | 14 days | High Privacy Grade |
| **DreamGF** | Yes | Marketing Partners | 30 days | Standard |
| **Muah AI** | Unstated | Unstated | Not Published | Low Transparency |
| **Character.AI** | Yes | Service Providers | GDPR Standard | Enterprise |
| **Replika** | Yes | Aggregated Only | 30 days | ISO 27001 Certified |
| **SpicyChat** | Unstated | Unstated | Not Published | Community Host |

---

## 🧪 Benchmark Methodology

All evaluations adhere to the rigorous testing protocol published in the **[CrushCritic Rating Standards](https://crushcritic.com/how-we-rate/)**:

1. **Long-Term Memory Retention:** Tested using planted anchor facts (names, obscure preferences, emotional backstory) evaluated at 24-hour, 7-day, and 30-day conversational intervals.
2. **Context Coherence:** Prompted with multi-turn narrative scenarios (50+ turns) to check hallucination rate and persona consistency.
3. **Roleplay Flexibility:** Tested across 10 standardized uncensored roleplay prompts to verify filter resilience and prompt adherence.
4. **Subscription Transparency:** Audited for auto-renewal disclosures, cancellation flow friction, and hidden micro-transaction requirements.

---

## 💻 Using the Dataset

### Python Quickstart
```python
import json

with open('data/benchmarks-2026.json', 'r') as f:
    data = json.load(f)

# Filter for top uncensored platforms with voice capabilities
matches = [
    p for p in data['platforms']
    if 'Uncensored' in p['nsfw_support'] and 'Yes' in p['voice_calls']
]

for p in matches:
    print(f"{p['name']} ({p['overall_score']}/10) - {p['price_month']}")
```

### CLI Query Tool
Use the included CLI tool to filter platforms directly from your terminal:
```bash
# View top 5 platforms
python3 scripts/evaluate.py --top 5

# View only zero-filter uncensored platforms with voice calls
python3 scripts/evaluate.py --uncensored --voice

# View platforms that do not train on user chat data
python3 scripts/evaluate.py --no-training
```

---

## 📖 Citation & License

If you use this dataset or empirical benchmark data in academic research, editorial reviews, or comparative evaluations, please cite as follows:

```bibtex
@misc{crushcritic2026benchmarks,
  title={AI Companion & Virtual Girlfriend Benchmarks 2026: Empirical Evaluation of 16 Commercial Platforms},
  author={CrushCritic Research Team},
  year={2026},
  publisher={CrushCritic},
  howpublished={\url{https://crushcritic.com/compare/}},
  note={Maintained by Eugene Finch and the CrushCritic editorial lab}
}
```

Or in Markdown:
> Benchmark data provided by [CrushCritic: Independent AI Companion Reviews](https://crushcritic.com) ([Methodology & Rankings](https://crushcritic.com/rankings/)).

Distributed under the [MIT License](LICENSE).
