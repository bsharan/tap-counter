# Tap-Counter roadmap: 26 Oct – 1 Dec 2026
Each row is a **GitHub Milestone**. Each task is a **GitHub Issue**, done on its own **branch**, merged by **Pull Request**
after CI passes. That's how product companies work.

| Week | Milestone | Issues (one PR each) | System skill it teaches |
|---|---|---|---|
| **26 Oct – 1 Nov** | M1: Repo like a pro | Push the repo · CI green · first Issue → branch → PR → merge · Wokwi: 3 item buttons count | Git flow, CI, code review |
| **2 – 8 Nov** | M2: Device talks to cloud | ESP32 → MQTT · Lambda handler wraps `Shop.tap` (+ tests) · **structured JSON logging** | Event-driven design, logging |
| **9 – 15 Nov** | M3: Live on AWS | IoT Core → Lambda → DynamoDB in Learner Lab · **idempotency** (a duplicate MQTT message must not double-count) · measure **Lambda cold start** | Reliability, cold starts, retries |
| **16 – 22 Nov** | M4: Owner sees value | Kitchen-screen page (S3) · night summary · **show ONE stall owner** · Data Engineer workshop for students | Product thinking, customer feedback |
| **23 Nov – 1 Dec** | M5: v0.1 release | Terraform for the whole stack · README with a demo GIF · tag `v0.1.0` · LinkedIn post | IaC, releases |

**Fixed dates inside this window:** Oct MoM **28 Oct** · Salesforce **30 Oct** · 2nd-year hackathon **6 Nov** ·
Launchpad badges **24 Nov** · lab exam **27–28 Nov**.

## Student workshop (Week 4): "From shop sales to insights: a data pipeline on AWS"
Built on your **AWS Data Engineer – Associate** certification. 4 hours, hands-on, in Learner Lab.
Tap-Counter sales (JSON) → **S3** → **Glue crawler** → **Athena SQL** ("which hour sells most chai?") → a simple chart.
Check beforehand that Glue and Athena work in Learner Lab.
Appraisal: Workshops for our Students (0.25 per hour). It also supports your Data Engineer certification claim.
