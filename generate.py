#!/usr/bin/env python3
"""Generate the Manufacturing Excellence Knowledge Base HTML."""

import json

# ============================
# DATA: All categories, topics and their detailed content
# ============================

categories = [
    {
        "id": "foundations",
        "title": "Foundations",
        "icon": "foundation",
        "topics": [
            {
                "id": "what-is-mfg-excellence",
                "title": "What is Manufacturing Excellence?",
                "tags": ["Overview", "Strategy"],
                "summary": "Core philosophy, principles, and pillars of manufacturing excellence as a strategic framework.",
                "content": """
<h2>What is Manufacturing Excellence?</h2>
<p>Manufacturing Excellence is a holistic management philosophy aimed at achieving world-class performance in quality, cost, delivery, safety, and morale (QCDSM). It is not a single methodology but an integrated framework that draws from Lean, Six Sigma, TPM, and continuous improvement culture to create sustainable competitive advantage in manufacturing operations.</p>

<h3>The Five Pillars of Manufacturing Excellence</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">Q</div><div class="step-content"><h5>Quality</h5><p>Defect-free production through built-in quality (Jidoka), statistical process control, and prevention-based thinking. Target: zero defects, measured via PPM (Parts Per Million) defect rates, First Pass Yield (FPY), and Cost of Poor Quality (COPQ).</p></div></div>
<div class="process-step"><div class="step-number">C</div><div class="step-content"><h5>Cost</h5><p>Elimination of all forms of waste (Muda) to optimize total cost of manufacturing. Encompasses material yield, labor productivity, energy efficiency, overhead reduction, and inventory turns. Target: lowest total cost of ownership, not just unit cost.</p></div></div>
<div class="process-step"><div class="step-number">D</div><div class="step-content"><h5>Delivery</h5><p>On-time, in-full delivery performance to customers. Driven by production flow, scheduling discipline, and supply chain reliability. Measured via OTIF (On Time In Full), lead time, and schedule adherence. Target: >98% OTIF.</p></div></div>
<div class="process-step"><div class="step-number">S</div><div class="step-content"><h5>Safety</h5><p>Zero-harm workplace through hazard elimination, behavioral safety programs, and safety culture. Measured by LTIR (Lost Time Incident Rate), near-miss reporting, and safety audit scores. Safety is always the non-negotiable first priority.</p></div></div>
<div class="process-step"><div class="step-number">M</div><div class="step-content"><h5>Morale</h5><p>Engaged, empowered workforce that drives continuous improvement from the shop floor. Measured through employee engagement surveys, suggestion rates, absenteeism, and skill matrix completion. People are the engine of excellence.</p></div></div>
</div>

<h3>The Manufacturing Excellence Maturity Model</h3>
<table>
<tr><th>Level</th><th>Stage</th><th>Characteristics</th></tr>
<tr><td>1</td><td>Reactive</td><td>Firefighting mode. No standardized processes. Quality by inspection. High variability.</td></tr>
<tr><td>2</td><td>Managed</td><td>Basic standards established. SOPs in place. Some measurement systems. Department-level improvement.</td></tr>
<tr><td>3</td><td>Defined</td><td>Standardized processes across the plant. Lean tools deployed. Cross-functional improvement teams active.</td></tr>
<tr><td>4</td><td>Quantitatively Managed</td><td>Data-driven decision making. Statistical process control. Predictive maintenance. Integrated supply chain.</td></tr>
<tr><td>5</td><td>Optimizing (World-Class)</td><td>Continuous improvement culture embedded. Innovation-driven. Benchmarking against global best. Self-directed work teams.</td></tr>
</table>

<div class="info-box">
<div class="info-box-title">Key Insight</div>
<p>Manufacturing Excellence is not about implementing tools — it is about building a culture. Tools and techniques are enablers, but the real transformation comes from leadership commitment, frontline engagement, and relentless discipline in sustaining improvements.</p>
</div>
"""
            },
            {
                "id": "tps",
                "title": "Toyota Production System (TPS)",
                "tags": ["Toyota", "Lean", "Foundation"],
                "summary": "The original production system that inspired Lean manufacturing worldwide.",
                "content": """
<h2>Toyota Production System (TPS)</h2>
<p>The Toyota Production System, developed by Taiichi Ohno and Eiji Toyoda between the 1940s and 1970s, is the foundational management system from which Lean manufacturing was derived. TPS is built on two conceptual pillars: Just-in-Time (JIT) and Jidoka (Automation with a Human Touch), all resting on a base of Heijunka (production leveling) and standardized work.</p>

<h3>The TPS House</h3>
<p>The famous "TPS House" diagram represents the complete system as a structure:</p>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Roof</span><h4>Goal: Best Quality, Lowest Cost, Shortest Lead Time, Highest Safety, High Morale</h4></div>
<p>The roof represents the ultimate goals of TPS — all elements of the system work together to achieve these outcomes simultaneously, not in isolation.</p>
</div>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Pillar 1</span><h4>Just-in-Time (JIT)</h4></div>
<p>Produce only what is needed, when it is needed, in the quantity needed. JIT eliminates overproduction (the worst waste) through takt time, continuous flow, and pull systems (Kanban). The goal is to have the right part at the right place at the right time.</p>
<ul>
<li><strong>Takt Time:</strong> The rate at which products must be produced to match customer demand. Takt = Available Production Time / Customer Demand.</li>
<li><strong>Continuous Flow:</strong> One-piece flow where products move through the process without batching, queuing, or waiting.</li>
<li><strong>Pull System (Kanban):</strong> Downstream processes signal upstream processes to produce only when needed, preventing overproduction.</li>
</ul>
</div>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Pillar 2</span><h4>Jidoka (Autonomation)</h4></div>
<p>Automation with a human touch — machines and operators have the authority and capability to detect abnormalities and stop production immediately. This builds quality into the process rather than inspecting it in at the end.</p>
<ul>
<li><strong>Andon:</strong> Visual signal system allowing any worker to stop the line when a problem is detected.</li>
<li><strong>Poka-Yoke:</strong> Error-proofing devices that prevent defects from occurring or progressing.</li>
<li><strong>Root Cause Analysis:</strong> When the line stops, the problem is analyzed to its root cause (5 Whys) and a permanent countermeasure is implemented.</li>
</ul>
</div>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Foundation</span><h4>Heijunka, Standardized Work, Kaizen</h4></div>
<p>The foundation supports both pillars. Heijunka (production leveling) smooths out volume and mix fluctuations. Standardized Work defines the current best-known method for each process. Kaizen (continuous improvement) systematically improves these standards.</p>
</div>

<h3>14 Principles of the Toyota Way</h3>
<p>Jeffrey Liker codified the philosophy behind TPS into 14 principles across four categories (the 4P model):</p>

<h4>Philosophy (Long-term thinking)</h4>
<ol>
<li>Base management decisions on a long-term philosophy, even at the expense of short-term financial goals.</li>
</ol>

<h4>Process (Eliminate waste)</h4>
<ol start="2">
<li>Create a continuous process flow to bring problems to the surface.</li>
<li>Use "pull" systems to avoid overproduction.</li>
<li>Level out the workload (Heijunka).</li>
<li>Build a culture of stopping to fix problems, to get quality right the first time (Jidoka).</li>
<li>Standardized tasks and processes are the foundation for continuous improvement and employee empowerment.</li>
<li>Use visual control so no problems are hidden.</li>
<li>Use only reliable, thoroughly tested technology that serves your people and processes.</li>
</ol>

<h4>People & Partners (Respect and grow)</h4>
<ol start="9">
<li>Grow leaders who thoroughly understand the work, live the philosophy, and teach it to others.</li>
<li>Develop exceptional people and teams who follow your company's philosophy.</li>
<li>Respect your extended network of partners and suppliers by challenging them and helping them improve.</li>
</ol>

<h4>Problem Solving (Continuous improvement)</h4>
<ol start="12">
<li>Go and see for yourself to thoroughly understand the situation (Genchi Genbutsu / Gemba).</li>
<li>Make decisions slowly by consensus, thoroughly considering all options; implement decisions rapidly (Nemawashi).</li>
<li>Become a learning organization through relentless reflection (Hansei) and continuous improvement (Kaizen).</li>
</ol>

<div class="info-box">
<div class="info-box-title">Why TPS Matters</div>
<p>TPS is not just a production system — it is a complete management system and philosophy. Many organizations adopt Lean tools superficially without embracing the underlying thinking. True TPS implementation requires a fundamental shift in leadership behavior, problem-solving discipline, and respect for people.</p>
</div>
"""
            },
            {
                "id": "lean-manufacturing",
                "title": "Lean Manufacturing",
                "tags": ["Lean", "Waste", "Flow"],
                "summary": "Systematic elimination of waste and creation of value flow in manufacturing operations.",
                "content": """
<h2>Lean Manufacturing</h2>
<p>Lean Manufacturing is a systematic methodology for eliminating waste within a manufacturing system while simultaneously delivering value to the customer. The term "Lean" was coined by John Krafcik in 1988 and popularized by Womack, Jones, and Roos in "The Machine That Changed the World" (1990). Lean is derived from the Toyota Production System but has been adapted and extended for global application.</p>

<h3>The Five Lean Principles</h3>
<p>Womack and Jones defined five core principles in "Lean Thinking" (1996):</p>
<div class="process-steps">
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Define Value</h5><p>Value is defined solely from the customer's perspective — what the customer is willing to pay for. Everything else is waste. This requires deeply understanding the customer's needs, not assuming them. Value must be expressed in terms of a specific product or service that meets the customer's needs at a specific price and time.</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Map the Value Stream</h5><p>Identify every step in the entire value stream for each product family, from raw material to customer delivery, and eliminate steps that do not create value. Value Stream Mapping (VSM) is the primary tool for this analysis.</p></div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Create Flow</h5><p>Make the value-creating steps flow smoothly without interruptions, detours, backflows, waiting, or batching. This often requires rethinking departmental boundaries and batch-and-queue thinking.</p></div></div>
<div class="process-step"><div class="step-number">4</div><div class="step-content"><h5>Establish Pull</h5><p>Let the customer pull value from the next upstream activity. Nothing is produced by an upstream process until the downstream customer signals a need. This is the antithesis of "push" production based on forecasts.</p></div></div>
<div class="process-step"><div class="step-number">5</div><div class="step-content"><h5>Seek Perfection</h5><p>There is no end state — perfection is the horizon. As waste is removed and flow improves, new wastes become visible. The cycle of improvement never ends. Perfection is the asymptotic goal that drives relentless improvement.</p></div></div>
</div>

<h3>The 8 Wastes of Lean (TIM WOODS / DOWNTIME)</h3>
<p>Originally Taiichi Ohno identified 7 wastes; the 8th (unused talent) was added later. Two popular mnemonics are TIM WOODS and DOWNTIME:</p>
<table>
<tr><th>Waste</th><th>Japanese</th><th>Description</th><th>Manufacturing Example</th></tr>
<tr><td>Transport</td><td>—</td><td>Unnecessary movement of materials or products between processes</td><td>Parts moved across the plant between non-adjacent workstations</td></tr>
<tr><td>Inventory</td><td>—</td><td>Excess raw materials, WIP, or finished goods beyond what is needed</td><td>3 months of safety stock when 2 weeks would suffice</td></tr>
<tr><td>Motion</td><td>—</td><td>Unnecessary movement of people (reaching, bending, walking)</td><td>Operator walking 20 steps to fetch tools not at the workstation</td></tr>
<tr><td>Waiting</td><td>—</td><td>Idle time when processes, people, or parts are not moving</td><td>Machine idle while operator waits for material delivery</td></tr>
<tr><td>Overproduction</td><td>—</td><td>Producing more, earlier, or faster than the customer needs</td><td>Making 500 units when the order is for 300</td></tr>
<tr><td>Overprocessing</td><td>—</td><td>Performing work beyond what the customer requires or values</td><td>Polishing a surface that will be hidden in the final assembly</td></tr>
<tr><td>Defects</td><td>—</td><td>Products or services that do not meet specifications</td><td>Rework, scrap, returns, warranty claims</td></tr>
<tr><td>Skills (Unused Talent)</td><td>—</td><td>Not utilizing people's skills, ideas, and creativity</td><td>Experienced operators not involved in problem-solving</td></tr>
</table>

<div class="info-box">
<div class="info-box-title">Overproduction: The Mother of All Waste</div>
<p>Taiichi Ohno considered overproduction the worst waste because it triggers all other wastes — excess inventory, extra transport, additional storage space, more handling, more defect opportunities, and masks problems by creating buffers that hide issues.</p>
</div>

<h3>Three Categories of Activity</h3>
<ul>
<li><strong>Value-Added (VA):</strong> Activities that transform material or information in a way the customer is willing to pay for. Typically only 5-10% of total lead time.</li>
<li><strong>Non-Value-Added but Necessary (NVAN):</strong> Activities required by current technology, regulations, or business processes but not valued by the customer (e.g., inspection, regulatory compliance). Minimize these.</li>
<li><strong>Non-Value-Added (NVA):</strong> Pure waste. Eliminate these immediately.</li>
</ul>

<h3>Lean vs. Traditional Manufacturing</h3>
<div class="comparison-grid">
<div class="comparison-col positive">
<h5>Lean Approach</h5>
<ul>
<li>Small batch sizes, ideally one-piece flow</li>
<li>Pull production based on actual demand</li>
<li>Decentralized decision-making</li>
<li>Multi-skilled, empowered operators</li>
<li>Continuous improvement culture</li>
<li>Low inventory, fast turns</li>
<li>Quality built into the process</li>
</ul>
</div>
<div class="comparison-col negative">
<h5>Traditional Approach</h5>
<ul>
<li>Large batch sizes for "efficiency"</li>
<li>Push production based on forecasts</li>
<li>Centralized command and control</li>
<li>Specialized, narrow-skilled workers</li>
<li>Improvement by management edict</li>
<li>High inventory as "safety net"</li>
<li>Quality by end-of-line inspection</li>
</ul>
</div>
</div>
"""
            },
            {
                "id": "six-sigma",
                "title": "Six Sigma",
                "tags": ["Quality", "Statistical", "DMAIC"],
                "summary": "Data-driven methodology for eliminating defects and reducing process variation.",
                "content": """
<h2>Six Sigma</h2>
<p>Six Sigma is a disciplined, data-driven methodology for eliminating defects and reducing variation in any process. Developed by Motorola engineer Bill Smith in 1986 and popularized by Jack Welch at General Electric in the 1990s, Six Sigma aims to achieve a process capability where the nearest specification limit is at least 6 standard deviations from the process mean — translating to no more than 3.4 defects per million opportunities (DPMO).</p>

<h3>The Statistical Foundation</h3>
<table>
<tr><th>Sigma Level</th><th>DPMO</th><th>Yield (%)</th><th>Capability</th></tr>
<tr><td>1σ</td><td>690,000</td><td>30.85%</td><td>Very poor</td></tr>
<tr><td>2σ</td><td>308,537</td><td>69.15%</td><td>Poor</td></tr>
<tr><td>3σ</td><td>66,807</td><td>93.32%</td><td>Average</td></tr>
<tr><td>4σ</td><td>6,210</td><td>99.38%</td><td>Good</td></tr>
<tr><td>5σ</td><td>233</td><td>99.977%</td><td>Excellent</td></tr>
<tr><td>6σ</td><td>3.4</td><td>99.9997%</td><td>World-class</td></tr>
</table>

<h3>DMAIC Methodology</h3>
<p>DMAIC is the core problem-solving framework of Six Sigma for improving existing processes:</p>

<div class="process-steps">
<div class="process-step"><div class="step-number">D</div><div class="step-content"><h5>Define</h5><p>Clearly articulate the problem, the customer, the process, and the project goals. Key tools: Project Charter, SIPOC Diagram (Suppliers, Inputs, Process, Outputs, Customers), Voice of the Customer (VOC), CTQ (Critical to Quality) tree. Define the scope, timeline, team, and expected financial impact.</p></div></div>
<div class="process-step"><div class="step-number">M</div><div class="step-content"><h5>Measure</h5><p>Quantify the current process performance using reliable data. Establish a baseline. Key tools: Data Collection Plan, Measurement System Analysis (MSA / Gage R&R), Process Mapping, Pareto Charts, Descriptive Statistics. Validate the measurement system before drawing conclusions from data.</p></div></div>
<div class="process-step"><div class="step-number">A</div><div class="step-content"><h5>Analyze</h5><p>Identify root causes of defects and variation using statistical analysis. Key tools: Fishbone Diagram (Ishikawa), 5 Whys, Hypothesis Testing, Regression Analysis, ANOVA, FMEA, Multi-Vari Studies. Separate vital few causes from the trivial many.</p></div></div>
<div class="process-step"><div class="step-number">I</div><div class="step-content"><h5>Improve</h5><p>Develop, pilot, and implement solutions to address root causes. Key tools: Design of Experiments (DOE), Brainstorming, Solution Selection Matrix, Pilot Testing, Process Simulation. Verify improvement with data, not intuition.</p></div></div>
<div class="process-step"><div class="step-number">C</div><div class="step-content"><h5>Control</h5><p>Sustain the gains by monitoring the improved process. Key tools: Control Charts (SPC), Control Plan, Standard Operating Procedures (SOPs), Response Plan, Process Dashboards. Hand over to process owners with documentation and training.</p></div></div>
</div>

<h3>DMADV (Design for Six Sigma)</h3>
<p>For designing new processes or products (rather than improving existing ones):</p>
<ul>
<li><strong>Define:</strong> Define design goals consistent with customer demands and enterprise strategy.</li>
<li><strong>Measure:</strong> Measure and identify CTQs, product capabilities, production process capability, and risks.</li>
<li><strong>Analyze:</strong> Analyze to develop and design alternatives.</li>
<li><strong>Design:</strong> Design an improved alternative, best suited per analysis in the previous step.</li>
<li><strong>Verify:</strong> Verify the design, set up pilot runs, implement the production process and hand over to process owner.</li>
</ul>

<h3>Six Sigma Belt System</h3>
<table>
<tr><th>Belt</th><th>Role</th><th>Training</th></tr>
<tr><td>White Belt</td><td>Awareness-level understanding, supports project teams</td><td>1-2 days</td></tr>
<tr><td>Yellow Belt</td><td>Participates in projects, understands basic tools</td><td>1-2 weeks</td></tr>
<tr><td>Green Belt</td><td>Leads smaller projects while maintaining regular role</td><td>2-3 weeks</td></tr>
<tr><td>Black Belt</td><td>Full-time improvement leader, mentors Green Belts</td><td>4-5 weeks</td></tr>
<tr><td>Master Black Belt</td><td>Strategic deployment, trains Black Belts, enterprise-level</td><td>Extensive experience</td></tr>
<tr><td>Champion</td><td>Executive sponsor, removes barriers, allocates resources</td><td>1-2 days executive training</td></tr>
</table>

<div class="info-box">
<div class="info-box-title">Lean Six Sigma</div>
<p>Lean Six Sigma combines the waste-elimination focus of Lean with the variation-reduction rigor of Six Sigma. Lean addresses speed and flow; Six Sigma addresses accuracy and consistency. Together, they provide a comprehensive toolkit for manufacturing improvement. Most modern manufacturing excellence programs use an integrated Lean Six Sigma approach.</p>
</div>
"""
            },
            {
                "id": "tpm",
                "title": "Total Productive Maintenance (TPM)",
                "tags": ["Maintenance", "OEE", "Reliability"],
                "summary": "Proactive maintenance philosophy maximizing equipment effectiveness through total employee involvement.",
                "content": """
<h2>Total Productive Maintenance (TPM)</h2>
<p>Total Productive Maintenance is a holistic approach to equipment maintenance that strives to achieve perfect production — no breakdowns, no slow running, no defects — through the participation of all employees. Developed by Seiichi Nakajima at JIPM (Japan Institute of Plant Maintenance) in the 1970s, TPM integrates maintenance into the daily work of production.</p>

<h3>The 8 Pillars of TPM</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Autonomous Maintenance (Jishu Hozen)</h5><p>Operators take ownership of basic maintenance tasks — cleaning, inspecting, lubricating, and tightening. This develops operator "equipment consciousness" and frees maintenance technicians for advanced work. The 7-step AM approach: initial cleaning → countermeasures for sources of contamination → develop cleaning/lubrication standards → general inspection training → autonomous inspection → workplace organization → full autonomous maintenance.</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Planned Maintenance</h5><p>Scheduled maintenance based on failure rates and equipment history. Evolves from time-based to condition-based to predictive maintenance. Goal: zero unplanned breakdowns. Uses MTBF (Mean Time Between Failures) and MTTR (Mean Time To Repair) as key metrics.</p></div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Quality Maintenance (Hinshitsu Hozen)</h5><p>Achieving zero defects by understanding the relationship between equipment conditions and product quality. Uses QM Matrix to map defect types to equipment components and process parameters. Establishes equipment conditions that prevent defects rather than detect them.</p></div></div>
<div class="process-step"><div class="step-number">4</div><div class="step-content"><h5>Focused Improvement (Kobetsu Kaizen)</h5><p>Cross-functional teams tackle chronic losses using structured problem-solving. Targets the "16 Major Losses" in equipment, manpower, and material yield. Uses tools like Why-Why Analysis, PM Analysis, and FMEA.</p></div></div>
<div class="process-step"><div class="step-number">5</div><div class="step-content"><h5>Early Equipment Management</h5><p>Apply lessons learned from existing equipment to the design and commissioning of new equipment. Goal: vertical startup — new equipment reaches planned performance in minimum time. Uses MP (Maintenance Prevention) design principles.</p></div></div>
<div class="process-step"><div class="step-number">6</div><div class="step-content"><h5>Training & Education</h5><p>Develop multi-skilled operators and maintenance technicians. Skill matrix management, one-point lessons (OPL), and on-the-job training. Target: every operator can detect, analyze, and address basic equipment abnormalities.</p></div></div>
<div class="process-step"><div class="step-number">7</div><div class="step-content"><h5>Safety, Health & Environment</h5><p>Zero accidents, zero pollution. Equipment-related hazard identification, risk assessment, and elimination. Environmental compliance and energy conservation integrated into maintenance activities.</p></div></div>
<div class="process-step"><div class="step-number">8</div><div class="step-content"><h5>TPM in Office/Administration</h5><p>Apply TPM principles to administrative and support processes. Eliminate losses in planning, scheduling, purchasing, and information flow. Improve the "administrative machine."</p></div></div>
</div>

<h3>OEE — Overall Equipment Effectiveness</h3>
<p>OEE is the gold-standard metric for measuring manufacturing productivity. It identifies the percentage of planned production time that is truly productive.</p>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Formula</span><h4>OEE = Availability × Performance × Quality</h4></div>
<ul>
<li><strong>Availability</strong> = (Run Time / Planned Production Time) × 100%. Losses: breakdowns, setup & adjustment.</li>
<li><strong>Performance</strong> = (Ideal Cycle Time × Total Count / Run Time) × 100%. Losses: small stops, reduced speed.</li>
<li><strong>Quality</strong> = (Good Count / Total Count) × 100%. Losses: startup rejects, production rejects.</li>
</ul>
<p>World-class OEE benchmark: 85%+ (90% Availability × 95% Performance × 99% Quality).</p>
</div>

<h3>The Six Big Losses</h3>
<table>
<tr><th>Category</th><th>Loss</th><th>Description</th></tr>
<tr><td rowspan="2">Availability</td><td>Equipment Failure</td><td>Unplanned breakdowns causing >10 min downtime</td></tr>
<tr><td>Setup & Adjustment</td><td>Changeover time, warm-up, adjustments</td></tr>
<tr><td rowspan="2">Performance</td><td>Idling & Minor Stops</td><td>Brief stops <10 min (jams, misfeeds, cleaning)</td></tr>
<tr><td>Reduced Speed</td><td>Running below design speed (wear, capability)</td></tr>
<tr><td rowspan="2">Quality</td><td>Process Defects</td><td>Scrap and rework during stable production</td></tr>
<tr><td>Startup Losses</td><td>Defects during warm-up until stable production</td></tr>
</table>
"""
            }
        ]
    },
    {
        "id": "lean-tools",
        "title": "Lean Tools & Techniques",
        "icon": "tools",
        "topics": [
            {
                "id": "vsm",
                "title": "Value Stream Mapping (VSM)",
                "tags": ["Flow", "Analysis", "Mapping"],
                "summary": "End-to-end visualization of material and information flow to identify waste and improvement opportunities.",
                "content": """
<h2>Value Stream Mapping (VSM)</h2>
<p>Value Stream Mapping is a Lean management tool that visually maps the flow of materials and information from supplier to customer through all process steps. It reveals the current state of operations, highlights sources of waste, and enables teams to design an improved future state. VSM was popularized by Mike Rother and John Shook in "Learning to See" (1998).</p>

<h3>Current State Map Components</h3>
<table>
<tr><th>Element</th><th>Symbol</th><th>Information Captured</th></tr>
<tr><td>Process Box</td><td>Rectangle</td><td>Cycle time (C/T), changeover time (C/O), uptime, batch size, number of operators, EPE (Every Product Every interval)</td></tr>
<tr><td>Inventory Triangle</td><td>Triangle with quantity</td><td>Amount of inventory between processes, measured in pieces and days of supply</td></tr>
<tr><td>Push Arrow</td><td>Striped arrow</td><td>Material pushed from one process to the next regardless of downstream need</td></tr>
<tr><td>Pull Arrow</td><td>Hollow arrow</td><td>Material pulled by downstream process signal</td></tr>
<tr><td>Supermarket</td><td>Open rectangle with lanes</td><td>Controlled inventory point for pull system</td></tr>
<tr><td>FIFO Lane</td><td>Rectangle labeled FIFO</td><td>First-in-first-out inventory lane with max quantity</td></tr>
<tr><td>Information Flow</td><td>Straight/zigzag arrows</td><td>Straight = electronic, zigzag = manual information</td></tr>
<tr><td>Timeline</td><td>Bottom zigzag</td><td>Value-added time (lower) vs. non-value-added time (upper)</td></tr>
</table>

<h3>VSM Process Steps</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Select Product Family</h5><p>Choose a product family that shares similar processing steps and equipment. Use a product-process matrix to identify families. Focus on the family that represents the highest volume or revenue.</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Walk the Process (Gemba Walk)</h5><p>Walk the entire value stream from shipping dock back to receiving dock. Observe actual conditions, don't rely on process documents. Record real cycle times, inventory levels, batch sizes, changeover times, uptime, and staffing.</p></div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Draw Current State Map</h5><p>Map material flow (left to right), information flow (right to left), and the timeline at the bottom. Include supplier, customer, production control, and all process steps. Always draw by hand first — pencil and paper, not software.</p></div></div>
<div class="process-step"><div class="step-number">4</div><div class="step-content"><h5>Analyze Waste & Opportunities</h5><p>Calculate total lead time vs. total processing time. Identify the biggest gaps (usually inventory wait time). Identify bottlenecks (longest cycle time). Flag quality issues, changeover losses, and information flow delays.</p></div></div>
<div class="process-step"><div class="step-number">5</div><div class="step-content"><h5>Design Future State Map</h5><p>Apply Lean principles: produce to takt time, implement continuous flow where possible, use supermarkets where flow isn't possible, send the customer schedule to one pacemaker process, level the production mix, and level the production volume.</p></div></div>
<div class="process-step"><div class="step-number">6</div><div class="step-content"><h5>Create Implementation Plan</h5><p>Break the future state into implementation loops. Start with the pacemaker loop (closest to customer). Define projects, owners, timelines, and metrics for each loop.</p></div></div>
</div>

<h3>Key VSM Metrics</h3>
<ul>
<li><strong>Lead Time:</strong> Total time from raw material receipt to finished goods shipment. Typically 95%+ is non-value-added.</li>
<li><strong>Processing Time:</strong> Sum of all value-added cycle times. Usually a tiny fraction of lead time.</li>
<li><strong>Value-Added Ratio:</strong> Processing Time / Lead Time × 100%. World-class target: >25% (most start at 1-5%).</li>
<li><strong>Takt Time:</strong> Available production time / customer demand per period.</li>
<li><strong>Inventory Days:</strong> Inventory quantity / daily demand. Shows how many days of demand each buffer represents.</li>
</ul>
"""
            },
            {
                "id": "five-s",
                "title": "5S Workplace Organization",
                "tags": ["Organization", "Visual", "Foundation"],
                "summary": "Five-step methodology for creating and maintaining organized, clean, high-performance workplaces.",
                "content": """
<h2>5S Workplace Organization</h2>
<p>5S is a systematic approach to workplace organization that creates the foundation for all other Lean improvements. A well-organized workplace makes problems visible, reduces waste, and establishes the discipline needed for continuous improvement. 5S is often the first Lean tool implemented because it is visible, tangible, and builds momentum.</p>

<h3>The Five Steps</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Seiri (Sort)</h5><p>Separate needed items from unneeded items and remove everything not required for current operations. Use red tags to identify items for removal — if in doubt, tag it. Establish a "red tag holding area" with a 30-day deadline. If it hasn't been needed in 30 days, dispose of it. This includes tools, fixtures, materials, documents, furniture, and equipment.</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Seiton (Set in Order / Straighten)</h5><p>A place for everything and everything in its place. Arrange needed items so they are easy to find, use, and return. Use shadow boards for tools, labeled locations for materials, and visual indicators for proper placement. Apply the principle of "minimum hand motion" — the most frequently used items should be within arm's reach. Use the ABC principle: A items (used hourly) at workstation, B items (used daily) nearby, C items (used weekly) in storage.</p></div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Seiso (Shine / Sweep)</h5><p>Clean the workplace thoroughly and maintain cleanliness as a form of inspection. Cleaning is not just about appearance — it is about detecting abnormalities: oil leaks, loose bolts, worn belts, cracks, and other early warning signs. Assign cleaning zones with responsible owners. Create cleaning checklists with daily, weekly, and monthly tasks. "Clean to inspect, inspect to detect, detect to correct."</p></div></div>
<div class="process-step"><div class="step-number">4</div><div class="step-content"><h5>Seiketsu (Standardize)</h5><p>Create standards and visual controls to maintain the first three S's. Develop 5S checklists with photographic standards showing "what good looks like." Color-code zones, pipes, and equipment. Create min/max indicators for inventory. Post standards at the point of use. Use floor markings (yellow for walkways, white for inventory areas, red for defect/quarantine zones).</p></div></div>
<div class="process-step"><div class="step-number">5</div><div class="step-content"><h5>Shitsuke (Sustain / Self-Discipline)</h5><p>Build habits and discipline to maintain standards permanently. This is the hardest step. Conduct regular 5S audits (weekly initially, then monthly). Post audit scores publicly. Integrate 5S into daily management routines. Recognize and celebrate good 5S practices. The goal is to make 5S "the way we work" rather than a periodic event.</p></div></div>
</div>

<h3>5S Audit Scoring</h3>
<table>
<tr><th>Score</th><th>Level</th><th>Description</th></tr>
<tr><td>1</td><td>Poor</td><td>Conditions are unsatisfactory, no evidence of 5S activity</td></tr>
<tr><td>2</td><td>Below Average</td><td>Some effort but inconsistent, many areas needing improvement</td></tr>
<tr><td>3</td><td>Average</td><td>Standards exist and are partially followed, room for improvement</td></tr>
<tr><td>4</td><td>Good</td><td>Standards well-maintained, minor deviations only</td></tr>
<tr><td>5</td><td>Excellent</td><td>Benchmark condition, self-sustaining, model area</td></tr>
</table>

<div class="info-box">
<div class="info-box-title">Safety as the 6th S</div>
<p>Many organizations add a 6th S for Safety, making it 6S. Safety is integrated into every step: Sort out hazardous materials, Set in order for ergonomic access, Shine to eliminate slip/trip hazards, Standardize safety procedures, and Sustain safety awareness. Some organizations use 7S (adding Security) or even 8S (adding Satisfaction).</p>
</div>
"""
            },
            {
                "id": "kaizen",
                "title": "Kaizen & Continuous Improvement",
                "tags": ["Improvement", "Culture", "Events"],
                "summary": "Philosophy and practice of continuous incremental improvement involving everyone in the organization.",
                "content": """
<h2>Kaizen & Continuous Improvement</h2>
<p>Kaizen (改善) literally translates to "change for better" in Japanese. In manufacturing, it represents both a philosophy (everyone, everywhere, every day improving) and a set of practices (structured improvement events). Kaizen is the engine of the Toyota Production System and the most fundamental concept in Lean manufacturing.</p>

<h3>Kaizen vs. Kaikaku</h3>
<div class="comparison-grid">
<div class="comparison-col positive">
<h5>Kaizen (Incremental)</h5>
<ul>
<li>Small, continuous improvements</li>
<li>Low risk, low cost</li>
<li>Everyone participates</li>
<li>Uses existing resources</li>
<li>Requires discipline and persistence</li>
<li>Builds culture over time</li>
<li>Example: Reducing changeover by 5 minutes</li>
</ul>
</div>
<div class="comparison-col negative">
<h5>Kaikaku (Radical)</h5>
<ul>
<li>Large, breakthrough improvements</li>
<li>Higher risk, higher investment</li>
<li>Led by specialists/management</li>
<li>May require new technology/layout</li>
<li>Produces dramatic results quickly</li>
<li>Needs Kaizen to sustain</li>
<li>Example: Complete line redesign with automation</li>
</ul>
</div>
</div>

<h3>Kaizen Event (Kaizen Blitz / Rapid Improvement Event)</h3>
<p>A focused, time-boxed improvement activity (typically 3-5 days) where a cross-functional team identifies and implements improvements to a specific process area.</p>
<div class="process-steps">
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Pre-Event Planning (2-4 weeks before)</h5><p>Define scope and objectives. Select team (6-10 members, mix of operators, engineers, supervisors, and outsiders). Collect baseline data. Prepare materials and logistics. Communicate to affected areas.</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Day 1: Understand Current State</h5><p>Train the team on Lean concepts. Walk the process (Gemba). Document current state with time observations, spaghetti diagrams, and waste identification. Establish baseline metrics.</p></div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Day 2-3: Analyze & Improve</h5><p>Brainstorm improvements. Prioritize using impact/effort matrix. Implement changes immediately — move equipment, reorganize workstations, create new standard work. "Just do it" mentality for low-risk changes.</p></div></div>
<div class="process-step"><div class="step-number">4</div><div class="step-content"><h5>Day 4: Test & Refine</h5><p>Run the improved process. Time the new cycle times. Identify remaining issues. Make adjustments. Document new standard work with photos and instructions.</p></div></div>
<div class="process-step"><div class="step-number">5</div><div class="step-content"><h5>Day 5: Present & Plan Sustainability</h5><p>Present results to management (before/after data). Create a 30-60-90 day action plan for remaining items. Assign owners for sustainability checks. Celebrate the team's achievements.</p></div></div>
</div>

<h3>Daily Kaizen (Kaizen Teian / Suggestion System)</h3>
<p>Beyond events, true Kaizen culture is built through daily small improvements:</p>
<ul>
<li><strong>Kaizen Teian (Suggestion System):</strong> Every employee submits improvement ideas. Target: 1 suggestion per person per month. Implement >80% of suggestions within 30 days. Focus on quantity over quality of ideas initially — build the habit of thinking about improvement.</li>
<li><strong>Kaizen Boards:</strong> Visual boards at each workstation where operators post improvement ideas, track status, and celebrate completions.</li>
<li><strong>Before/After Photos:</strong> Simple documentation showing the improvement. Powerful for recognition and sharing knowledge across shifts.</li>
<li><strong>PDCA Cycle:</strong> Plan → Do → Check → Act. The scientific method applied to improvement. Every Kaizen should follow this cycle.</li>
</ul>

<div class="info-box">
<div class="info-box-title">The Kaizen Mindset</div>
<p>"The message of Kaizen is that not a day should go by without some kind of improvement being made somewhere in the company." — Masaaki Imai. The goal is not perfection but relentless progress. A 1% improvement every day compounds to a 37x improvement over a year.</p>
</div>
"""
            },
            {
                "id": "kanban",
                "title": "Kanban System",
                "tags": ["Pull", "Visual", "Inventory"],
                "summary": "Visual signaling system for managing production flow and inventory using pull-based principles.",
                "content": """
<h2>Kanban System</h2>
<p>Kanban (看板, meaning "visual signal" or "card") is a scheduling system for Lean and Just-in-Time manufacturing. Developed by Taiichi Ohno at Toyota, Kanban controls the logistical chain from a production point of view, serving as a demand-driven scheduling system rather than a supply-driven one.</p>

<h3>Kanban Principles</h3>
<ul>
<li><strong>Visualize workflow:</strong> Make all work and its status visible to everyone.</li>
<li><strong>Limit Work in Progress (WIP):</strong> Do not start new work until current work is pulled downstream.</li>
<li><strong>Manage flow:</strong> Monitor and optimize the smooth movement of work through the system.</li>
<li><strong>Make policies explicit:</strong> Rules for how work flows must be clearly defined and understood.</li>
<li><strong>Implement feedback loops:</strong> Regular reviews of flow, quality, and throughput.</li>
<li><strong>Improve collaboratively:</strong> Use the system to identify bottlenecks and improve together.</li>
</ul>

<h3>Types of Kanban</h3>
<table>
<tr><th>Type</th><th>Purpose</th><th>Mechanism</th></tr>
<tr><td>Production Kanban</td><td>Signals upstream process to produce more parts</td><td>Card attached to empty container returned to producing process</td></tr>
<tr><td>Withdrawal Kanban</td><td>Authorizes movement of parts from supermarket to downstream process</td><td>Card authorizes picking from supermarket inventory</td></tr>
<tr><td>Signal Kanban</td><td>Triggers production of a batch (for batch processes like stamping)</td><td>Triangular card placed at reorder point in supermarket</td></tr>
<tr><td>Supplier Kanban</td><td>Signals external supplier to deliver materials</td><td>Card or electronic signal sent to supplier</td></tr>
<tr><td>Emergency Kanban</td><td>Issued temporarily for defective parts, machine trouble, or extra demand</td><td>Red-tagged card withdrawn at end of period</td></tr>
</table>

<h3>Kanban Calculation</h3>
<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Formula</span><h4>Number of Kanbans = (Daily Demand × Lead Time × Safety Factor) / Container Quantity</h4></div>
<p>Where:</p>
<ul>
<li><strong>Daily Demand (D):</strong> Average daily usage of the part</li>
<li><strong>Lead Time (L):</strong> Time from Kanban signal to replenishment (in days), including processing, waiting, and transport time</li>
<li><strong>Safety Factor (S):</strong> Buffer for variability, typically 1.0 (no buffer) to 1.5 (high variability). Start high and reduce as stability improves.</li>
<li><strong>Container Quantity (C):</strong> Number of parts per container. Should be <10% of daily demand for frequent replenishment.</li>
</ul>
</div>

<h3>Kanban Rules (Toyota's 6 Rules)</h3>
<ol>
<li>Downstream processes withdraw items from upstream only in the quantity specified by the Kanban.</li>
<li>Upstream processes produce items only in the quantity and sequence indicated by the Kanban.</li>
<li>No items are produced or moved without a Kanban.</li>
<li>A Kanban must always accompany each item.</li>
<li>Defective products are never sent to the next process.</li>
<li>The number of Kanbans is reduced over time to expose problems and drive improvement.</li>
</ol>
"""
            },
            {
                "id": "smed",
                "title": "SMED (Single Minute Exchange of Die)",
                "tags": ["Changeover", "Setup", "Flexibility"],
                "summary": "Methodology for dramatically reducing equipment changeover time to enable small-batch production.",
                "content": """
<h2>SMED — Single Minute Exchange of Die</h2>
<p>SMED is a systematic approach to reducing changeover time developed by Shigeo Shingo. "Single minute" means single-digit minutes (under 10 minutes), not literally one minute. SMED enables small-batch production, increases machine availability, and provides the flexibility needed for mixed-model production.</p>

<h3>Why Changeover Reduction Matters</h3>
<p>Long changeovers force large batch sizes (to "justify" the setup time), which creates excess inventory, long lead times, and inflexibility. Reducing changeover time enables:</p>
<ul>
<li>Smaller batch sizes → less inventory → shorter lead times</li>
<li>More frequent changeovers → more product variety → better customer responsiveness</li>
<li>Higher machine availability → increased capacity without capital investment</li>
<li>EPE (Every Product Every) interval reduction → from EPE-week to EPE-day or EPE-shift</li>
</ul>

<h3>The SMED Methodology</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">0</div><div class="step-content"><h5>Preliminary Stage: Internal & External Not Distinguished</h5><p>In the current state, all changeover activities are mixed together. Film the entire changeover. Document every step, duration, and who performs it. This is the baseline — typically changeovers take 1-4 hours.</p></div></div>
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Stage 1: Separate Internal and External Setup</h5><p><strong>Internal setup:</strong> Activities that can only be done while the machine is stopped (e.g., physically changing the die). <strong>External setup:</strong> Activities that can be done while the machine is still running (e.g., gathering tools, preheating, staging the next die). Simply separating these and doing external setup while the machine runs typically reduces changeover by 30-50%.</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Stage 2: Convert Internal to External Setup</h5><p>Re-examine every internal element and find ways to convert them to external. Examples: pre-heat molds externally, use standardized fixture heights so no adjustment is needed, pre-assemble tooling, use intermediate jigs. This can reduce changeover by another 50%.</p></div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Stage 3: Streamline All Setup Operations</h5><p>Optimize remaining internal and external elements. Use parallel operations (two people working simultaneously). Replace bolts with quick-release clamps. Eliminate adjustments through precision engineering. Use one-touch setups and cassette systems. Target: single-digit minutes.</p></div></div>
</div>

<h3>SMED Techniques</h3>
<table>
<tr><th>Technique</th><th>Principle</th><th>Example</th></tr>
<tr><td>Use of quick-release mechanisms</td><td>Replace bolts and screws with cams, toggle clamps, or quarter-turn fasteners</td><td>C-clamps replacing 12 bolts on a die</td></tr>
<tr><td>Standardization of functions</td><td>Standardize die heights, clamp positions, and locating fixtures</td><td>All dies the same height, eliminating stroke adjustment</td></tr>
<tr><td>Parallel operations</td><td>Two people performing tasks simultaneously on different sides</td><td>Two operators each working one side of a press die</td></tr>
<tr><td>Eliminating adjustments</td><td>Use fixed numerical settings, stoppers, and gauges instead of trial-and-error</td><td>Digital position readouts replacing manual alignment</td></tr>
<tr><td>Mechanization</td><td>Use hydraulic, pneumatic, or motorized systems for heavy lifting/clamping</td><td>Hydraulic die cart replacing manual crane positioning</td></tr>
</table>
"""
            },
            {
                "id": "poka-yoke",
                "title": "Poka-Yoke (Error-Proofing)",
                "tags": ["Quality", "Prevention", "Jidoka"],
                "summary": "Design techniques that prevent mistakes from becoming defects in manufacturing processes.",
                "content": """
<h2>Poka-Yoke (Error-Proofing)</h2>
<p>Poka-Yoke (ポカヨケ) means "mistake-proofing" in Japanese. Developed by Shigeo Shingo as part of the Toyota Production System, Poka-Yoke devices and techniques are designed to either prevent errors from occurring or detect them immediately before they become defects. The philosophy is that defects are caused by human errors, and the system should make it impossible or immediately obvious when an error occurs.</p>

<h3>Types of Poka-Yoke</h3>
<table>
<tr><th>Type</th><th>Action</th><th>Description</th><th>Example</th></tr>
<tr><td>Prevention (Control)</td><td>Makes error impossible</td><td>Physical design prevents the wrong action from being performed</td><td>USB connector can only be inserted one way; asymmetric bolt pattern on a fixture</td></tr>
<tr><td>Detection (Warning)</td><td>Alerts when error occurs</td><td>Sensor or check detects the error and signals the operator</td><td>Weight check after assembly alerts if a part is missing; color-coded connectors</td></tr>
<tr><td>Shutdown</td><td>Stops the process</td><td>Automatic stop when error is detected, preventing defective output</td><td>Machine stops if sensor detects missing component before assembly</td></tr>
</table>

<h3>Poka-Yoke Detection Methods</h3>
<ul>
<li><strong>Contact Method:</strong> Physical shape, size, or feature detection. Example: guide pins that only allow correct orientation.</li>
<li><strong>Fixed-Value Method:</strong> Ensures the correct number of actions are performed. Example: a parts tray with exactly the right number of compartments — if any are left filled, a step was missed.</li>
<li><strong>Motion-Step Method:</strong> Ensures operations are performed in the correct sequence. Example: a sensor system that only enables the next tool after the previous operation is confirmed complete.</li>
</ul>

<h3>Poka-Yoke Design Principles</h3>
<ol>
<li><strong>Simple and inexpensive:</strong> The best Poka-Yoke devices cost almost nothing — a guide pin, a color code, a physical stop.</li>
<li><strong>Part of the process:</strong> Integrated into the operation, not an added inspection step.</li>
<li><strong>Close to the source:</strong> Detect errors at the point where they occur, not downstream.</li>
<li><strong>100% inspection:</strong> Check every unit, not just samples (unlike statistical sampling).</li>
<li><strong>Immediate feedback:</strong> Alert the operator instantly so corrective action can be taken.</li>
</ol>

<h3>Examples in Manufacturing</h3>
<ul>
<li><strong>Asymmetric mounting holes:</strong> Parts can only be assembled in the correct orientation.</li>
<li><strong>Limit switches:</strong> Machine won't operate unless guards are in place.</li>
<li><strong>Color-coded wiring:</strong> Each wire has a unique color matching its destination.</li>
<li><strong>Go/No-Go gauges:</strong> Parts that don't meet tolerance physically can't pass through the gauge.</li>
<li><strong>Bin counting systems:</strong> Kitting trays with shaped cavities for each component — empty cavities indicate missing parts.</li>
<li><strong>Bar code verification:</strong> Scanner confirms correct part number before assembly.</li>
<li><strong>Torque-limited tools:</strong> Wrench clicks when correct torque is reached, preventing over-tightening.</li>
</ul>
"""
            },
            {
                "id": "andon",
                "title": "Andon & Visual Management",
                "tags": ["Visual", "Signals", "Transparency"],
                "summary": "Visual control systems that make the status of production visible and enable rapid response to abnormalities.",
                "content": """
<h2>Andon & Visual Management</h2>
<p>Andon (行灯, meaning "lantern") is a visual control system that alerts team leaders and management to quality or process problems on the production floor. More broadly, visual management is the principle of making all aspects of production visible so that anyone can instantly understand the current status and identify abnormalities.</p>

<h3>Andon System Components</h3>
<ul>
<li><strong>Andon Cord/Button:</strong> Every workstation has a cord or button that any operator can pull/press to signal a problem. This activates the Andon board and typically plays a musical tone unique to the zone.</li>
<li><strong>Andon Board:</strong> A large, visible display (typically overhead) showing the status of each station/zone. Green = normal, Yellow = assistance needed, Red = line stopped.</li>
<li><strong>Response Protocol:</strong> When Andon is triggered, the team leader must respond within the takt time. If the problem is resolved within takt, the line continues. If not, the line stops at the next fixed position.</li>
</ul>

<h3>Visual Management Tools</h3>
<table>
<tr><th>Tool</th><th>Purpose</th><th>Implementation</th></tr>
<tr><td>Production boards</td><td>Track hourly/daily production vs. plan</td><td>Whiteboard with hourly slots showing planned vs. actual, with reason codes for misses</td></tr>
<tr><td>Floor markings</td><td>Define locations and flow paths</td><td>Yellow = walkways, white = storage, red = reject, green = finished goods</td></tr>
<tr><td>Shadow boards</td><td>Tool organization and missing item detection</td><td>Outlined silhouettes of tools on pegboard — missing tool is immediately visible</td></tr>
<tr><td>Color-coded signals</td><td>Equipment and material status</td><td>Green/yellow/red lights on machines, color-coded inventory bins</td></tr>
<tr><td>KPI dashboards</td><td>Real-time performance visibility</td><td>Large displays showing OEE, quality rate, output, safety metrics</td></tr>
<tr><td>Standard work displays</td><td>Process instructions at point of use</td><td>Laminated sheets with photos, sequence, timing, and key quality checks</td></tr>
<tr><td>Kanban boards</td><td>Work-in-progress status</td><td>Cards or indicators showing what's in process, what's waiting, what's done</td></tr>
</table>

<h3>Visual Factory Principles</h3>
<ol>
<li><strong>5-Second Rule:</strong> Anyone walking through the area should be able to understand the current status in 5 seconds or less.</li>
<li><strong>Abnormality Detection:</strong> Visual standards make it immediately obvious when something is wrong — deviation from standard is the trigger for action.</li>
<li><strong>Information at Point of Use:</strong> All information needed to perform work should be visible where the work happens, not in an office binder.</li>
<li><strong>Self-Explaining:</strong> The workplace should explain itself without verbal instruction. A new employee should understand the basic flow and rules by looking around.</li>
</ol>
"""
            },
            {
                "id": "standardized-work",
                "title": "Standardized Work",
                "tags": ["Standards", "Baseline", "Takt"],
                "summary": "Documented current best practice that provides a baseline for continuous improvement.",
                "content": """
<h2>Standardized Work</h2>
<p>Standardized Work is the documentation and practice of the current best-known method for performing a job. It is not about rigid compliance to prevent creativity — it is about establishing a stable baseline from which to improve. Without a standard, there is no basis for improvement (no way to know if a change is better or worse). Standardized work is the foundation of Kaizen.</p>

<h3>Three Elements of Standardized Work</h3>
<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Element 1</span><h4>Takt Time</h4></div>
<p>The rate at which products must be completed to meet customer demand. Takt Time = Net Available Working Time per Period / Customer Demand per Period. Example: 460 min available / 230 units demand = 2 min takt. Every operator's work must be balanced to takt time.</p>
</div>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Element 2</span><h4>Work Sequence</h4></div>
<p>The specific order in which an operator performs the manual steps of a job within one takt cycle. This is the most efficient sequence considering safety, quality, and time. It includes walking, picking up parts, operating machines, performing checks, and placing finished work.</p>
</div>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Element 3</span><h4>Standard Work-in-Process (SWIP)</h4></div>
<p>The minimum inventory of parts needed at each workstation to maintain smooth flow. This includes parts in machines and between processes. SWIP ensures the operator always has work to do without building excess inventory.</p>
</div>

<h3>Standardized Work Documents</h3>
<table>
<tr><th>Document</th><th>Content</th><th>Purpose</th></tr>
<tr><td>Production Capacity Sheet</td><td>Machine cycle times, manual times, tool change intervals for each process</td><td>Identifies bottlenecks and overall capacity</td></tr>
<tr><td>Standardized Work Combination Table</td><td>Man-machine timing chart showing manual work, machine work, and walking for one cycle</td><td>Balances operator work to takt time, shows wait time and opportunities</td></tr>
<tr><td>Standardized Work Chart (Layout)</td><td>Workstation layout showing operator movement path, machine locations, quality checks, and safety points</td><td>Visual representation of the work sequence in the physical space</td></tr>
<tr><td>Job Element Sheet</td><td>Detailed breakdown of each step with key points and reasons</td><td>Training document for operators — the "why" behind each step</td></tr>
</table>

<h3>Key Principles</h3>
<ul>
<li><strong>Operator-created:</strong> Standards should be developed with the people who do the work, not imposed by engineers from an office.</li>
<li><strong>Living documents:</strong> Updated every time a Kaizen improvement is made — the new standard becomes the new baseline.</li>
<li><strong>Posted at the workstation:</strong> Visible and accessible, not filed in a cabinet.</li>
<li><strong>Audited regularly:</strong> Leaders observe work and compare to the standard. Deviations trigger coaching or standard updates.</li>
</ul>
"""
            },
            {
                "id": "jit",
                "title": "Just-in-Time (JIT)",
                "tags": ["Flow", "Pull", "Inventory"],
                "summary": "Production strategy producing only what is needed, when needed, in the quantity needed.",
                "content": """
<h2>Just-in-Time (JIT)</h2>
<p>Just-in-Time is a production strategy where materials, parts, and products are produced and delivered exactly when they are needed — not before, not after. JIT is one of the two pillars of the Toyota Production System, and its implementation requires the integration of several Lean tools: Kanban, Heijunka, SMED, and continuous flow.</p>

<h3>JIT Prerequisites</h3>
<ul>
<li><strong>Stable, reliable processes:</strong> Machines must be available when needed (TPM), and quality must be built in (Jidoka).</li>
<li><strong>Leveled production (Heijunka):</strong> Demand fluctuations are smoothed to create a steady, predictable workload.</li>
<li><strong>Quick changeovers (SMED):</strong> Small batches are only economical when changeover time is short.</li>
<li><strong>Pull system (Kanban):</strong> Production is triggered by actual consumption, not forecasts.</li>
<li><strong>Reliable suppliers:</strong> Material deliveries must be frequent, on-time, and defect-free.</li>
<li><strong>Capable workforce:</strong> Multi-skilled operators who can flex across processes.</li>
</ul>

<h3>Heijunka (Production Leveling)</h3>
<p>Heijunka is the foundation that makes JIT possible by leveling both volume and product mix:</p>

<div class="comparison-grid">
<div class="comparison-col positive">
<h5>Leveled Production</h5>
<ul>
<li>Monday: AABABC</li>
<li>Tuesday: AABABC</li>
<li>Wednesday: AABABC</li>
<li>Smooth, predictable demand on all upstream processes</li>
</ul>
</div>
<div class="comparison-col negative">
<h5>Batch Production</h5>
<ul>
<li>Monday: AAAAAA</li>
<li>Tuesday: BBBBBB</li>
<li>Wednesday: CCCCCC</li>
<li>Spiky demand creates overload/underload on upstream</li>
</ul>
</div>
</div>

<p>The <strong>Heijunka Box</strong> is a physical scheduling tool — a grid of slots organized by time period (columns) and product type (rows). Kanban cards are placed in slots to create a leveled production sequence. The material handler withdraws cards at regular pitch intervals and delivers them to the production line.</p>

<h3>Continuous Flow (One-Piece Flow)</h3>
<p>The ideal state of JIT is one-piece flow — each unit moves immediately from one process step to the next without batching, queuing, or storage. Benefits:</p>
<ul>
<li>Shortest possible lead time</li>
<li>Immediate defect detection (no batch to quarantine)</li>
<li>Minimum work-in-process inventory</li>
<li>Balanced workload across operators</li>
<li>Immediate visibility of problems</li>
</ul>
"""
            }
        ]
    },
    {
        "id": "quality",
        "title": "Quality Management",
        "icon": "quality",
        "topics": [
            {
                "id": "tqm",
                "title": "Total Quality Management (TQM)",
                "tags": ["Quality", "Culture", "Customer"],
                "summary": "Organization-wide approach to long-term quality improvement through customer focus and continuous improvement.",
                "content": """
<h2>Total Quality Management (TQM)</h2>
<p>TQM is a management approach that places quality at the center of all organizational activities. Influenced by Deming, Juran, Crosby, and Ishikawa, TQM integrates quality into every function — from product design to customer service — and involves every employee in the pursuit of excellence.</p>

<h3>8 Principles of TQM</h3>
<ol>
<li><strong>Customer Focus:</strong> Quality is defined by the customer. Understand and exceed customer expectations.</li>
<li><strong>Total Employee Involvement:</strong> Every person at every level participates in quality improvement.</li>
<li><strong>Process-Centered:</strong> Focus on processes that deliver results, not just outcomes.</li>
<li><strong>Integrated System:</strong> All functions and departments work as interconnected processes.</li>
<li><strong>Strategic & Systematic Approach:</strong> Quality improvement is planned and aligned with business strategy.</li>
<li><strong>Continual Improvement:</strong> A permanent objective of the organization (Kaizen).</li>
<li><strong>Fact-Based Decision Making:</strong> Decisions are based on data analysis, not opinion.</li>
<li><strong>Communications:</strong> Effective communication ensures awareness, alignment, and engagement.</li>
</ol>

<h3>Deming's 14 Points for Management</h3>
<ol>
<li>Create constancy of purpose toward improvement of product and service.</li>
<li>Adopt the new philosophy — management must learn their responsibilities and take on leadership for change.</li>
<li>Cease dependence on inspection to achieve quality — build quality into the process.</li>
<li>End the practice of awarding business on price tag alone; instead, minimize total cost by working with a single supplier.</li>
<li>Improve constantly and forever every process for planning, production, and service.</li>
<li>Institute training on the job.</li>
<li>Adopt and institute leadership — help people do a better job.</li>
<li>Drive out fear so everyone can work effectively.</li>
<li>Break down barriers between departments.</li>
<li>Eliminate slogans, exhortations, and targets for the workforce — they create adversarial relationships.</li>
<li>Eliminate numerical quotas for the workforce and numerical goals for management.</li>
<li>Remove barriers that rob people of pride of workmanship — abolish the annual rating/merit system.</li>
<li>Institute a vigorous program of education and self-improvement for everyone.</li>
<li>Put everybody in the company to work to accomplish the transformation.</li>
</ol>

<h3>Quality Management Tools (7 QC Tools)</h3>
<table>
<tr><th>Tool</th><th>Purpose</th><th>When to Use</th></tr>
<tr><td>Check Sheet</td><td>Structured data collection</td><td>Gathering data systematically for analysis</td></tr>
<tr><td>Pareto Chart</td><td>Identify vital few vs. trivial many</td><td>Prioritizing problems or causes (80/20 rule)</td></tr>
<tr><td>Fishbone Diagram (Ishikawa)</td><td>Root cause analysis</td><td>Brainstorming potential causes (Man, Machine, Method, Material, Measurement, Mother Nature — 6M)</td></tr>
<tr><td>Histogram</td><td>Show frequency distribution</td><td>Understanding process variation and centering</td></tr>
<tr><td>Scatter Diagram</td><td>Show relationship between variables</td><td>Testing for correlation between cause and effect</td></tr>
<tr><td>Control Chart</td><td>Monitor process stability over time</td><td>Distinguishing special cause from common cause variation (SPC)</td></tr>
<tr><td>Flowchart</td><td>Visualize process steps</td><td>Understanding process flow and identifying complexity</td></tr>
</table>
"""
            },
            {
                "id": "spc",
                "title": "Statistical Process Control (SPC)",
                "tags": ["Statistics", "Control Charts", "Variation"],
                "summary": "Application of statistical methods to monitor and control manufacturing processes.",
                "content": """
<h2>Statistical Process Control (SPC)</h2>
<p>SPC uses statistical methods to monitor and control a process, ensuring it operates at its full potential to produce conforming product. Pioneered by Walter Shewhart in the 1920s and championed by W. Edwards Deming, SPC distinguishes between common cause variation (inherent to the process) and special cause variation (assignable to specific factors).</p>

<h3>Types of Variation</h3>
<div class="comparison-grid">
<div class="comparison-col positive">
<h5>Common Cause (Random)</h5>
<ul>
<li>Inherent in the process design</li>
<li>Consistent, predictable variation</li>
<li>Affects all output uniformly</li>
<li>Can only be reduced by changing the process itself</li>
<li>Example: Natural material variation, ambient temperature changes</li>
</ul>
</div>
<div class="comparison-col negative">
<h5>Special Cause (Assignable)</h5>
<ul>
<li>Not inherent — caused by specific events</li>
<li>Unpredictable, sporadic patterns</li>
<li>Assignable to identifiable factors</li>
<li>Can be eliminated by finding and removing the cause</li>
<li>Example: Worn tool, untrained operator, defective batch of material</li>
</ul>
</div>
</div>

<h3>Control Charts</h3>
<p>Control charts are the primary tool of SPC. A control chart plots process data over time against statistically calculated control limits (UCL and LCL), typically set at ±3 standard deviations from the mean.</p>

<table>
<tr><th>Chart Type</th><th>Data Type</th><th>Measures</th><th>Application</th></tr>
<tr><td>X-bar & R</td><td>Variable (continuous)</td><td>Mean & Range of subgroups</td><td>Most common; subgroup size 2-10</td></tr>
<tr><td>X-bar & S</td><td>Variable</td><td>Mean & Std Dev of subgroups</td><td>Subgroup size >10</td></tr>
<tr><td>I-MR (X-MR)</td><td>Variable</td><td>Individual values & Moving Range</td><td>When subgroups of 1 (batch processes, expensive testing)</td></tr>
<tr><td>p Chart</td><td>Attribute</td><td>Proportion defective</td><td>Pass/fail inspection, variable sample size</td></tr>
<tr><td>np Chart</td><td>Attribute</td><td>Number defective</td><td>Pass/fail inspection, constant sample size</td></tr>
<tr><td>c Chart</td><td>Attribute</td><td>Count of defects per unit</td><td>Defects per PCB, scratches per panel, constant area</td></tr>
<tr><td>u Chart</td><td>Attribute</td><td>Defects per unit</td><td>Same as c but variable area/sample size</td></tr>
</table>

<h3>Process Capability (Cp, Cpk)</h3>
<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Formulas</span><h4>Process Capability Indices</h4></div>
<ul>
<li><strong>Cp = (USL - LSL) / (6σ):</strong> Measures potential capability — how much spread the process has relative to specification width. Does not account for centering. Cp ≥ 1.33 is the common minimum target.</li>
<li><strong>Cpk = min[(USL - μ) / (3σ), (μ - LSL) / (3σ)]:</strong> Measures actual capability — accounts for how well the process is centered. Cpk = Cp only when the process is perfectly centered. Cpk ≥ 1.33 is the common target; Cpk ≥ 1.67 for critical characteristics.</li>
<li><strong>Pp / Ppk:</strong> Same as Cp/Cpk but uses overall (long-term) standard deviation instead of within-subgroup. Used for preliminary studies before process is in statistical control.</li>
</ul>
</div>

<h3>Nelson Rules (Western Electric Rules)</h3>
<p>Beyond a single point outside control limits, these rules detect non-random patterns indicating special causes:</p>
<ol>
<li>One point beyond 3σ from the centerline</li>
<li>Nine consecutive points on one side of the centerline</li>
<li>Six consecutive points steadily increasing or decreasing (trend)</li>
<li>Fourteen consecutive points alternating up and down (systematic variation)</li>
<li>Two of three consecutive points beyond 2σ on the same side</li>
<li>Four of five consecutive points beyond 1σ on the same side</li>
<li>Fifteen consecutive points within 1σ of the centerline (stratification)</li>
<li>Eight consecutive points beyond 1σ on either side (mixture)</li>
</ol>
"""
            },
            {
                "id": "fmea",
                "title": "FMEA (Failure Mode & Effects Analysis)",
                "tags": ["Risk", "Prevention", "Design"],
                "summary": "Systematic methodology for identifying potential failure modes, their causes, and effects to prioritize preventive actions.",
                "content": """
<h2>FMEA — Failure Mode and Effects Analysis</h2>
<p>FMEA is a structured, systematic technique for failure analysis. It identifies potential failure modes in a system, product, or process, assesses their risk through severity, occurrence, and detection ratings, and prioritizes corrective actions. FMEA is a proactive tool — it is used before problems occur, not after.</p>

<h3>Types of FMEA</h3>
<table>
<tr><th>Type</th><th>Focus</th><th>When Used</th></tr>
<tr><td>Design FMEA (DFMEA)</td><td>Product/component design</td><td>During product development, before manufacturing begins</td></tr>
<tr><td>Process FMEA (PFMEA)</td><td>Manufacturing/assembly process</td><td>During process planning, before production starts</td></tr>
<tr><td>System FMEA</td><td>Complete system interactions</td><td>Early in system design to analyze interfaces</td></tr>
</table>

<h3>FMEA Columns (AIAG-VDA Format)</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Function / Requirement</h5><p>What is the process step or design function? What must it do?</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Potential Failure Mode</h5><p>How could the function fail? (e.g., missing hole, wrong dimension, incomplete weld, cross-threaded bolt)</p></div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Potential Effect(s) of Failure</h5><p>What happens if the failure occurs? Impact on customer, downstream process, safety, regulatory compliance.</p></div></div>
<div class="process-step"><div class="step-number">4</div><div class="step-content"><h5>Severity (S): 1-10</h5><p>How serious is the effect? 1 = no effect, 10 = safety hazard without warning. Determined by the worst potential effect.</p></div></div>
<div class="process-step"><div class="step-number">5</div><div class="step-content"><h5>Potential Cause(s) of Failure</h5><p>What could cause this failure mode? (e.g., worn tool, operator error, material variation, incorrect program)</p></div></div>
<div class="process-step"><div class="step-number">6</div><div class="step-content"><h5>Occurrence (O): 1-10</h5><p>How frequently is this cause likely to occur? 1 = extremely unlikely, 10 = almost certain.</p></div></div>
<div class="process-step"><div class="step-number">7</div><div class="step-content"><h5>Current Controls (Prevention & Detection)</h5><p>What controls are currently in place to prevent or detect this failure? List both prevention controls and detection controls.</p></div></div>
<div class="process-step"><div class="step-number">8</div><div class="step-content"><h5>Detection (D): 1-10</h5><p>How effective are current controls at detecting the failure before it reaches the customer? 1 = almost certain detection, 10 = no detection possible.</p></div></div>
</div>

<h3>Action Priority (AP) — AIAG-VDA Method</h3>
<p>The modern AIAG-VDA FMEA handbook (2019) replaced the traditional RPN (Risk Priority Number = S × O × D) with Action Priority (AP), which uses a lookup table to classify each failure mode as:</p>
<table>
<tr><th>Priority</th><th>Action Required</th></tr>
<tr><td>High (H)</td><td>Action is mandatory. Must reduce risk through design or process changes.</td></tr>
<tr><td>Medium (M)</td><td>Action should be taken. Improvement recommended based on engineering judgment.</td></tr>
<tr><td>Low (L)</td><td>Action may be taken at team's discretion. Current controls are adequate.</td></tr>
</table>

<div class="info-box">
<div class="info-box-title">Why AP Replaced RPN</div>
<p>The traditional RPN (S×O×D) had significant flaws: an RPN of 100 could be (10×10×1) or (5×5×4) — same number, vastly different risk profiles. The first is a critical safety issue with excellent detection, the other is a moderate issue with poor detection. The AP system uses structured logic to ensure high-severity failures always receive priority regardless of the multiplication outcome.</p>
</div>

<h3>8D Problem Solving</h3>
<p>When a failure does occur, 8D (Eight Disciplines) is the structured corrective action process:</p>
<ol>
<li><strong>D1:</strong> Establish the team — cross-functional, with process knowledge</li>
<li><strong>D2:</strong> Describe the problem — IS/IS NOT analysis, 5W2H</li>
<li><strong>D3:</strong> Develop interim containment actions — protect the customer immediately</li>
<li><strong>D4:</strong> Determine root cause — 5 Whys, Fishbone, Fault Tree Analysis</li>
<li><strong>D5:</strong> Choose permanent corrective actions — verify with data</li>
<li><strong>D6:</strong> Implement permanent corrective actions — validate effectiveness</li>
<li><strong>D7:</strong> Prevent recurrence — update FMEA, control plans, standards, training</li>
<li><strong>D8:</strong> Congratulate the team — recognize contributions</li>
</ol>
"""
            },
            {
                "id": "problem-solving",
                "title": "Root Cause Analysis & Problem Solving",
                "tags": ["Analysis", "5 Whys", "A3"],
                "summary": "Structured methods for identifying root causes and implementing permanent corrective actions.",
                "content": """
<h2>Root Cause Analysis & Problem Solving</h2>
<p>Effective problem solving is the cornerstone of manufacturing excellence. The goal is never just to fix the immediate symptom but to identify and eliminate the root cause so the problem never recurs. Multiple methodologies exist, each suited to different complexity levels.</p>

<h3>5 Whys Analysis</h3>
<p>The simplest and most widely used root cause tool. Ask "Why?" iteratively (typically 5 times, but as many as needed) until you reach the fundamental cause. Developed by Sakichi Toyoda.</p>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Example</span><h4>Machine stopped producing parts</h4></div>
<ul>
<li><strong>Why 1:</strong> The machine overheated. → <strong>Why?</strong></li>
<li><strong>Why 2:</strong> The cooling system wasn't circulating coolant. → <strong>Why?</strong></li>
<li><strong>Why 3:</strong> The coolant pump failed. → <strong>Why?</strong></li>
<li><strong>Why 4:</strong> The pump bearings wore out. → <strong>Why?</strong></li>
<li><strong>Why 5:</strong> The preventive maintenance schedule didn't include pump bearing inspection. → <strong>Root Cause!</strong></li>
</ul>
<p><strong>Countermeasure:</strong> Add pump bearing inspection to the PM schedule at the correct frequency based on manufacturer recommendations.</p>
</div>

<h3>A3 Problem Solving</h3>
<p>A structured problem-solving methodology that fits on a single A3-size paper (11×17 inches). It forces clear, concise thinking and tells the complete story of a problem and its resolution. Developed at Toyota as a communication and thinking tool.</p>

<table>
<tr><th>Section</th><th>Content</th></tr>
<tr><td>Title</td><td>Clear, specific problem statement</td></tr>
<tr><td>Background</td><td>Why this problem matters; business context and impact</td></tr>
<tr><td>Current Condition</td><td>Facts, data, process maps showing the current state; Pareto of defects/issues</td></tr>
<tr><td>Goal / Target</td><td>Specific, measurable target state (e.g., "Reduce scrap from 4.2% to 1.5% by Q3")</td></tr>
<tr><td>Root Cause Analysis</td><td>5 Whys, Fishbone, data analysis showing why the gap exists</td></tr>
<tr><td>Countermeasures</td><td>Specific actions to address root causes, with owners, dates, and expected impact</td></tr>
<tr><td>Implementation Plan</td><td>Timeline, milestones, and resource requirements</td></tr>
<tr><td>Follow-Up</td><td>Results tracking, confirmation of effectiveness, standardization of successful countermeasures</td></tr>
</table>

<h3>Fishbone (Ishikawa) Diagram — The 6Ms</h3>
<p>Organizes potential causes into categories for systematic brainstorming:</p>
<ul>
<li><strong>Man (People):</strong> Skill, training, fatigue, motivation, experience</li>
<li><strong>Machine (Equipment):</strong> Capability, wear, calibration, maintenance, age</li>
<li><strong>Method (Process):</strong> Procedures, work instructions, sequence, standards</li>
<li><strong>Material:</strong> Raw material quality, specifications, supplier variation, storage conditions</li>
<li><strong>Measurement:</strong> Gauges, calibration, MSA, measurement method, data accuracy</li>
<li><strong>Mother Nature (Environment):</strong> Temperature, humidity, cleanliness, lighting, vibration</li>
</ul>

<h3>Fault Tree Analysis (FTA)</h3>
<p>A top-down, deductive failure analysis using Boolean logic (AND/OR gates) to trace all possible paths to a top-level failure event. Used for complex system failures, safety-critical analysis, and when 5 Whys reveals multiple interacting causes. FTA provides a visual, logical structure showing how combinations of lower-level events lead to the undesired top event.</p>
"""
            }
        ]
    },
    {
        "id": "strategic",
        "title": "Strategic & Management Systems",
        "icon": "strategy",
        "topics": [
            {
                "id": "hoshin-kanri",
                "title": "Hoshin Kanri (Policy Deployment)",
                "tags": ["Strategy", "Alignment", "X-Matrix"],
                "summary": "Strategic planning process that aligns the entire organization around breakthrough objectives using catchball and the X-Matrix.",
                "content": """
<h2>Hoshin Kanri (Policy Deployment)</h2>
<p>Hoshin Kanri (方針管理) translates to "direction management" or "policy deployment." It is a strategic planning process that communicates, aligns, and cascades the organization's most important goals (breakthrough objectives) from top management to every level, ensuring everyone is working toward the same priorities. Hoshin Kanri bridges the gap between strategy and execution.</p>

<h3>Key Components</h3>
<ul>
<li><strong>True North (Vision):</strong> The long-term ideal state the organization is working toward — 10-30 year horizon.</li>
<li><strong>Breakthrough Objectives:</strong> 3-5 year strategic goals that represent significant step-changes toward True North. Limited to 3-5 objectives maximum.</li>
<li><strong>Annual Objectives:</strong> What must be achieved this year to make progress on breakthrough objectives.</li>
<li><strong>Improvement Priorities:</strong> The specific processes or areas that must be improved to achieve annual objectives.</li>
<li><strong>Targets & Metrics:</strong> Measurable indicators for each objective at every level.</li>
</ul>

<h3>The X-Matrix</h3>
<p>The X-Matrix is the signature tool of Hoshin Kanri — a single-page visual that shows the relationship between long-term objectives, annual objectives, improvement priorities, targets, and responsible owners. The four quadrants radiate from the center, with correlation matrices in the corners showing alignment.</p>

<table>
<tr><th>Quadrant</th><th>Content</th><th>Timeframe</th></tr>
<tr><td>South</td><td>Breakthrough Objectives (3-5 year)</td><td>Long-term</td></tr>
<tr><td>West</td><td>Annual Objectives</td><td>This year</td></tr>
<tr><td>North</td><td>Improvement Priorities / Top-Level Actions</td><td>Ongoing</td></tr>
<tr><td>East</td><td>Targets & KPIs to Improve</td><td>Measured continuously</td></tr>
<tr><td>Corners</td><td>Correlation dots showing alignment between adjacent quadrants</td><td>—</td></tr>
<tr><td>Far Right</td><td>Responsible owners for each improvement priority</td><td>—</td></tr>
</table>

<h3>Catchball Process</h3>
<p>Catchball is the iterative dialogue between organizational levels that turns top-down goals into actionable plans with bottom-up input. It is NOT a one-way cascade — it is a negotiation:</p>
<ol>
<li>Senior leadership sets breakthrough objectives and annual priorities</li>
<li>These are "thrown" to the next level for input on feasibility, approach, and resource needs</li>
<li>The next level "throws back" proposed actions, targets, and concerns</li>
<li>Dialogue continues until mutual agreement on objectives, methods, and resources</li>
<li>The process cascades further down, with each level defining its contribution</li>
</ol>

<h3>Annual Operating Plan (AOP)</h3>
<p>The AOP is the annual execution plan derived from Hoshin Kanri. It translates strategic objectives into departmental and functional plans with specific projects, budgets, timelines, and accountability. The AOP typically includes:</p>
<ul>
<li>Volume and revenue targets</li>
<li>Productivity improvement targets</li>
<li>Quality improvement targets</li>
<li>Capital expenditure plans</li>
<li>Workforce development plans</li>
<li>Key projects and their milestones</li>
</ul>

<h3>PDCA in Hoshin Kanri</h3>
<p>Hoshin Kanri follows the Deming Cycle at every level:</p>
<ul>
<li><strong>Plan:</strong> Set objectives, develop strategies, define KPIs</li>
<li><strong>Do:</strong> Execute the annual plan, implement improvement priorities</li>
<li><strong>Check:</strong> Monthly/quarterly reviews comparing actual vs. plan (Hoshin Reviews)</li>
<li><strong>Act:</strong> Adjust strategies based on reviews; carry forward learnings to next cycle</li>
</ul>
"""
            },
            {
                "id": "dwm",
                "title": "Daily Work Management (DWM)",
                "tags": ["Daily", "Routine", "Gemba"],
                "summary": "Structured system for managing and improving daily operations at every organizational level.",
                "content": """
<h2>Daily Work Management (DWM)</h2>
<p>Daily Work Management is the system of routines, standards, and escalation processes that ensures daily operations run smoothly while creating a framework for identifying and solving problems in real-time. While Hoshin Kanri handles strategic breakthrough goals, DWM manages the day-to-day performance that sustains the business.</p>

<h3>DWM Components</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Standard Work for Leaders</h5><p>Defined routines for supervisors, managers, and directors specifying what to check, where to go, and what to do at specific times. A first-line supervisor might spend 60% of their time on the Gemba (shop floor), with a structured routine: morning start-up check → Tier 1 meeting → Gemba walks → problem-solving → standard work audits → end-of-shift handover.</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Tiered Meeting Structure</h5><p>A cascading series of daily stand-up meetings that escalate information and problems from the shop floor to plant management:</p>
<ul>
<li><strong>Tier 1 (Team Level):</strong> 5-10 min at the workstation. Team leader + operators. Review past 24hrs (safety, quality, delivery, issues). Update the team board.</li>
<li><strong>Tier 2 (Department Level):</strong> 15 min in the department. Supervisors + support functions. Review Tier 1 escalations, departmental KPIs, resource needs.</li>
<li><strong>Tier 3 (Plant Level):</strong> 15-20 min at the plant war room. Department managers + plant manager. Review plant-wide performance, cross-functional issues, customer escalations.</li>
<li><strong>Tier 4 (Executive Level):</strong> Weekly/bi-weekly. Plant leadership + corporate. Strategic issues, multi-plant coordination, policy decisions.</li>
</ul>
</div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Visual Management Boards</h5><p>Each tier has a physical board displaying SQDC(M) metrics: Safety incidents/near-misses, Quality (scrap, rework, FPY), Delivery (OTIF, schedule adherence), Cost (efficiency, waste), and Morale (attendance, suggestions). Green/red status for each metric makes performance instantly visible.</p></div></div>
<div class="process-step"><div class="step-number">4</div><div class="step-content"><h5>Escalation & Problem-Solving Process</h5><p>Problems that cannot be resolved at one tier are escalated to the next. Each escalation includes: what happened, when, impact, containment action taken, and help needed. Problems are tracked on the board until permanently resolved.</p></div></div>
<div class="process-step"><div class="step-number">5</div><div class="step-content"><h5>Gemba Walks</h5><p>Leaders regularly walk the production floor to observe actual conditions, ask questions, and coach problem-solving. Gemba walks are not inspections — they are learning and coaching opportunities. Go see, ask why, show respect (the three principles of Gemba walks).</p></div></div>
</div>

<h3>DWM Success Factors</h3>
<ul>
<li><strong>Discipline:</strong> Meetings happen every day, at the same time, same place, same format. No skipping.</li>
<li><strong>Time-boxed:</strong> Meetings are short and focused — not problem-solving sessions. Problems are escalated or assigned for offline resolution.</li>
<li><strong>Visual:</strong> Information is on the wall, not in a computer. Anyone walking by can see the status.</li>
<li><strong>Two-way:</strong> Information flows up (problems, data) AND down (priorities, decisions, recognition).</li>
<li><strong>Action-oriented:</strong> Every meeting results in clear actions with owners and due dates.</li>
</ul>
"""
            },
            {
                "id": "bsc",
                "title": "Balanced Scorecard (BSC)",
                "tags": ["KPI", "Strategy", "Perspectives"],
                "summary": "Strategic performance management framework measuring organizational health across four perspectives.",
                "content": """
<h2>Balanced Scorecard (BSC)</h2>
<p>The Balanced Scorecard, developed by Robert Kaplan and David Norton in 1992, translates an organization's mission and strategy into a comprehensive set of performance measures across four perspectives. It ensures that financial measures are balanced with operational, customer, and learning metrics to give a complete picture of organizational health.</p>

<h3>The Four Perspectives</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">F</div><div class="step-content"><h5>Financial Perspective</h5><p>"How do we look to shareholders?" Measures: Revenue growth, operating margin, EBITDA, return on capital employed (ROCE), economic value added (EVA), cash flow. In manufacturing: cost per unit, material yield, inventory turns, total cost of ownership.</p></div></div>
<div class="process-step"><div class="step-number">C</div><div class="step-content"><h5>Customer Perspective</h5><p>"How do customers see us?" Measures: Customer satisfaction (CSAT), Net Promoter Score (NPS), on-time delivery (OTIF), quality (PPM, warranty claims), market share, customer retention, lead time.</p></div></div>
<div class="process-step"><div class="step-number">I</div><div class="step-content"><h5>Internal Process Perspective</h5><p>"What must we excel at?" Measures: OEE, first pass yield, cycle time, changeover time, scrap rate, process capability (Cpk), throughput, inventory accuracy, supply chain performance.</p></div></div>
<div class="process-step"><div class="step-number">L</div><div class="step-content"><h5>Learning & Growth Perspective</h5><p>"Can we continue to improve and create value?" Measures: Employee skill matrix completion, training hours per employee, suggestion rate, employee engagement, retention rate, IT system capability, innovation pipeline.</p></div></div>
</div>

<h3>Strategy Map</h3>
<p>A Strategy Map visually shows how objectives in each perspective connect through cause-and-effect relationships. Reading bottom-up: improved employee skills (Learning) → better process performance (Internal) → higher customer satisfaction (Customer) → improved financial results (Financial). This chain of causality is the logic model of the strategy.</p>

<h3>BSC in Manufacturing</h3>
<table>
<tr><th>Perspective</th><th>Objective Example</th><th>KPI</th><th>Target</th></tr>
<tr><td>Financial</td><td>Reduce manufacturing cost</td><td>Cost per unit produced</td><td>-8% year-over-year</td></tr>
<tr><td>Customer</td><td>Improve delivery reliability</td><td>OTIF %</td><td>≥98%</td></tr>
<tr><td>Internal Process</td><td>Increase equipment effectiveness</td><td>OEE %</td><td>≥85%</td></tr>
<tr><td>Learning & Growth</td><td>Develop multi-skilled workforce</td><td>% operators with 3+ skills</td><td>≥75%</td></tr>
</table>
"""
            },
            {
                "id": "gemba-management",
                "title": "Gemba & Shop Floor Management",
                "tags": ["Gemba", "Leadership", "Go-See"],
                "summary": "Principle of managing at the actual place where value is created — the shop floor.",
                "content": """
<h2>Gemba & Shop Floor Management</h2>
<p>Gemba (現場) means "the real place" — the actual location where work happens and value is created. In manufacturing, Gemba is the shop floor. Gemba management is the practice of going to where the work happens, observing actual conditions, understanding problems firsthand, and making decisions based on facts rather than reports.</p>

<h3>Genchi Genbutsu (Go and See for Yourself)</h3>
<p>A core Toyota principle: go to the source to find the facts to make correct decisions, build consensus, and achieve goals at the best speed. It means:</p>
<ul>
<li>Don't rely on second-hand reports or data alone — go see the actual situation.</li>
<li>Don't manage from a conference room — manage from where value is created.</li>
<li>Don't assume you know the answer — observe, ask questions, and understand deeply.</li>
</ul>

<h3>The Three Reals (San Gen Shugi)</h3>
<ul>
<li><strong>Genba (現場) — Real Place:</strong> Go to the actual location of the problem.</li>
<li><strong>Genbutsu (現物) — Real Thing:</strong> Examine the actual product, material, or machine involved.</li>
<li><strong>Genjitsu (現実) — Real Facts:</strong> Observe the actual data and conditions, not assumptions.</li>
</ul>

<h3>Gemba Walk Best Practices</h3>
<ol>
<li><strong>Have a purpose:</strong> Each walk should focus on a specific theme — safety, quality, flow, standard work adherence, 5S. Don't try to check everything every time.</li>
<li><strong>Follow a standard route:</strong> Cover different areas on different days so the entire plant is observed weekly.</li>
<li><strong>Observe before asking:</strong> Spend time watching the process before asking questions. Look for abnormalities — deviations from the standard.</li>
<li><strong>Ask "Why?", not "Who?":</strong> Focus on process problems, not blame. "Why did this happen?" not "Who caused this?"</li>
<li><strong>Coach, don't audit:</strong> Gemba walks are coaching opportunities, not inspections. Help people develop their problem-solving capabilities.</li>
<li><strong>Follow up:</strong> Any commitments made on the Gemba must be followed through. Loss of follow-up credibility destroys the entire system.</li>
</ol>

<h3>Kamishibai Boards</h3>
<p>A visual audit scheduling system using color-coded T-cards. Each card represents an audit task (5S check, safety check, standard work observation). Cards have green on one side and red on the other. Leaders flip cards as they complete audits, making it visible which audits are done (green) and which are pending (red). This ensures consistent Gemba presence and audit discipline.</p>
"""
            }
        ]
    },
    {
        "id": "advanced",
        "title": "Advanced Methods",
        "icon": "advanced",
        "topics": [
            {
                "id": "industry-4",
                "title": "Industry 4.0 & Smart Manufacturing",
                "tags": ["Digital", "IoT", "AI"],
                "summary": "The fourth industrial revolution — integrating cyber-physical systems, IoT, cloud computing, and AI into manufacturing.",
                "content": """
<h2>Industry 4.0 & Smart Manufacturing</h2>
<p>Industry 4.0 represents the fourth industrial revolution, characterized by the integration of digital technologies into manufacturing. It builds on the foundation of Lean and operational excellence, augmenting human decision-making with data, connectivity, and intelligent automation.</p>

<h3>Key Technologies</h3>
<table>
<tr><th>Technology</th><th>Application in Manufacturing</th><th>Impact</th></tr>
<tr><td>IoT (Internet of Things)</td><td>Sensors on machines collecting real-time data (temperature, vibration, pressure, cycle counts)</td><td>Condition monitoring, predictive maintenance, real-time OEE</td></tr>
<tr><td>Digital Twin</td><td>Virtual replica of physical assets, processes, or systems that updates in real-time</td><td>Process simulation, scenario testing, virtual commissioning</td></tr>
<tr><td>AI / Machine Learning</td><td>Pattern recognition in quality data, predictive analytics, demand forecasting</td><td>Predictive quality, autonomous optimization, anomaly detection</td></tr>
<tr><td>Robotics & Cobots</td><td>Collaborative robots working alongside humans for assembly, material handling, inspection</td><td>Ergonomic improvement, consistent quality, flexible automation</td></tr>
<tr><td>AGV/AMR</td><td>Automated Guided Vehicles / Autonomous Mobile Robots for material transport</td><td>Automated logistics, reduced forklift traffic, optimized flow</td></tr>
<tr><td>Additive Manufacturing</td><td>3D printing for prototyping, tooling, jigs, fixtures, and low-volume production</td><td>Rapid iteration, mass customization, reduced tooling cost</td></tr>
<tr><td>Cloud & Edge Computing</td><td>Data storage, analytics, and real-time processing at the machine edge or in the cloud</td><td>Scalable analytics, multi-plant visibility, reduced IT infrastructure</td></tr>
<tr><td>AR/VR</td><td>Augmented reality for operator guidance, remote expert assistance, training</td><td>Reduced training time, fewer errors, remote troubleshooting</td></tr>
</table>

<h3>Digital Transformation Roadmap</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Connect (Visibility)</h5><p>Instrument machines and processes with sensors. Establish data infrastructure. Create real-time dashboards. This is the "digital 5S" — making information visible.</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Analyze (Transparency)</h5><p>Use analytics to understand why things happen. Root cause analysis with data. Statistical modeling. Correlation analysis between process parameters and quality outcomes.</p></div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Predict (Preparedness)</h5><p>Use machine learning to predict future states. Predictive maintenance, quality prediction, demand forecasting. Move from reactive to proactive management.</p></div></div>
<div class="process-step"><div class="step-number">4</div><div class="step-content"><h5>Automate (Adaptability)</h5><p>Closed-loop autonomous optimization. Self-adjusting processes. Lights-out manufacturing. Human oversight of automated decision-making.</p></div></div>
</div>

<div class="info-box">
<div class="info-box-title">Lean Before Digital</div>
<p>Digitizing a broken process just gives you a faster broken process. Always stabilize and standardize operations with Lean fundamentals before adding digital technology. Industry 4.0 amplifies existing capabilities — it doesn't replace the need for operational discipline, standardized work, and continuous improvement culture.</p>
</div>
"""
            },
            {
                "id": "ergonomics",
                "title": "Ergonomics & Human Factors",
                "tags": ["Safety", "RULA", "REBA"],
                "summary": "Assessment and design of workstations for optimal human performance, safety, and well-being.",
                "content": """
<h2>Ergonomics & Human Factors</h2>
<p>Ergonomics (human factors engineering) is the science of designing workstations, tools, and tasks to fit human capabilities and limitations. In manufacturing, poor ergonomics leads to musculoskeletal disorders (MSDs), reduced productivity, higher absenteeism, and quality problems from operator fatigue and discomfort.</p>

<h3>Ergonomic Assessment Tools</h3>
<table>
<tr><th>Tool</th><th>Full Name</th><th>Focus</th><th>Output</th></tr>
<tr><td>RULA</td><td>Rapid Upper Limb Assessment</td><td>Upper body posture (neck, trunk, arms, wrists)</td><td>Score 1-7; Action levels: 1-2 acceptable, 3-4 investigate, 5-6 soon, 7 immediate change</td></tr>
<tr><td>REBA</td><td>Rapid Entire Body Assessment</td><td>Whole body posture including legs</td><td>Score 1-15; Risk levels: negligible to very high</td></tr>
<tr><td>NIOSH Lifting</td><td>NIOSH Revised Lifting Equation</td><td>Manual lifting tasks</td><td>Recommended Weight Limit (RWL) and Lifting Index (LI). LI > 1.0 indicates risk</td></tr>
<tr><td>OCRA</td><td>Occupational Repetitive Actions</td><td>Repetitive upper limb tasks</td><td>OCRA Index for risk of repetitive strain</td></tr>
<tr><td>Snook Tables</td><td>Liberty Mutual Tables</td><td>Push, pull, carry, and lift capacities</td><td>Acceptable force/weight for given % of population</td></tr>
</table>

<h3>Ergonomic Design Principles for Workstations</h3>
<ul>
<li><strong>Work Height:</strong> Precision work: 5-10 cm above elbow height. Light assembly: at elbow height. Heavy work: 10-15 cm below elbow height. Adjustable workstations accommodate all operators.</li>
<li><strong>Reach Zones:</strong> Primary zone (frequent reach): within forearm length. Secondary zone (occasional reach): within full arm length. Tertiary zone (rare reach): extended reach — minimize use.</li>
<li><strong>Reduce Repetitive Motion:</strong> Job rotation (every 2 hours), task variety, mechanized assists for repetitive tasks.</li>
<li><strong>Minimize Manual Material Handling:</strong> Use lifts, conveyors, tilt tables, vacuum lifters. Keep loads close to the body. Avoid twisting while lifting.</li>
<li><strong>Reduce Static Postures:</strong> Alternate sitting and standing. Provide anti-fatigue mats. Avoid sustained overhead work.</li>
<li><strong>Lighting:</strong> 300-500 lux for general assembly. 500-1000 lux for precision/inspection work. Eliminate glare and shadows.</li>
</ul>

<h3>Karakuri Kaizen</h3>
<p>Karakuri (からくり) is the Japanese art of using simple, low-cost mechanical devices (gravity, springs, levers, counterweights) to automate material handling and ergonomic assists without electricity or complex technology. Examples: gravity-fed parts chutes, counterweight-assisted lift fixtures, tilting work surfaces. Karakuri embodies the Lean philosophy of simple, elegant solutions.</p>
"""
            },
            {
                "id": "supply-chain",
                "title": "Supply Chain & Inventory Management",
                "tags": ["Inventory", "ABC-XYZ", "Logistics"],
                "summary": "Methods for optimizing material flow, inventory levels, and supplier relationships in manufacturing.",
                "content": """
<h2>Supply Chain & Inventory Management</h2>
<p>Effective supply chain and inventory management ensures the right materials are available at the right time and quantity while minimizing carrying costs, stockouts, and obsolescence. Lean supply chain principles extend the waste-elimination mindset beyond the factory walls.</p>

<h3>ABC-XYZ Inventory Classification</h3>
<div class="comparison-grid">
<div class="comparison-col positive">
<h5>ABC Analysis (Value)</h5>
<ul>
<li><strong>A Items (80/20 rule):</strong> ~20% of SKUs contributing ~80% of total value. High control, frequent review, accurate forecasting, JIT delivery.</li>
<li><strong>B Items:</strong> ~30% of SKUs contributing ~15% of value. Moderate control, periodic review, standard reorder points.</li>
<li><strong>C Items:</strong> ~50% of SKUs contributing ~5% of value. Simple controls, bulk ordering, higher safety stock acceptable.</li>
</ul>
</div>
<div class="comparison-col negative">
<h5>XYZ Analysis (Variability)</h5>
<ul>
<li><strong>X Items:</strong> Stable, predictable demand. Low forecast error (<20% CoV). Easy to plan, low safety stock needed.</li>
<li><strong>Y Items:</strong> Moderate demand variability. Medium forecast error (20-50% CoV). Moderate safety stock, periodic review.</li>
<li><strong>Z Items:</strong> Highly variable, unpredictable demand. High forecast error (>50% CoV). Difficult to forecast, make-to-order where possible.</li>
</ul>
</div>
</div>

<h3>Inventory Management Metrics</h3>
<table>
<tr><th>Metric</th><th>Formula</th><th>Target</th></tr>
<tr><td>Inventory Turns</td><td>COGS / Average Inventory Value</td><td>Higher is better (varies by industry: 4-12 typical for manufacturing)</td></tr>
<tr><td>Days of Inventory (DOI)</td><td>365 / Inventory Turns</td><td>Lower is better</td></tr>
<tr><td>Stock-out Rate</td><td>Number of stock-outs / Total demand events × 100</td><td><2%</td></tr>
<tr><td>Inventory Accuracy</td><td>Correct counts / Total counts × 100</td><td>≥98% for A items</td></tr>
<tr><td>Carrying Cost</td><td>Typically 20-30% of inventory value annually</td><td>Minimize through turns improvement</td></tr>
<tr><td>OTIF (On Time In Full)</td><td>Orders delivered on time AND complete / Total orders × 100</td><td>≥98%</td></tr>
</table>

<h3>Economic Order Quantity (EOQ)</h3>
<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Formula</span><h4>EOQ = √(2DS / H)</h4></div>
<ul>
<li><strong>D:</strong> Annual demand in units</li>
<li><strong>S:</strong> Fixed cost per order (setup cost + ordering cost)</li>
<li><strong>H:</strong> Annual holding cost per unit (storage + capital + obsolescence + insurance)</li>
</ul>
<p>EOQ finds the order quantity that minimizes total inventory cost (ordering cost + holding cost). Note: Lean thinking challenges EOQ by reducing S (setup cost) through SMED, which makes smaller, more frequent orders economical.</p>
</div>

<h3>Milk Run & Supplier Kanban</h3>
<p>Instead of each supplier delivering independently (creating variable truck arrivals and dock congestion), a Milk Run uses a dedicated route vehicle that visits multiple suppliers on a fixed schedule, picking up small quantities at each stop — like a milk delivery route. This enables frequent, small-lot deliveries aligned with production pull signals.</p>
"""
            },
            {
                "id": "design-for-manufacturing",
                "title": "Design for Manufacturing (DFM/DFA)",
                "tags": ["Design", "Assembly", "Cost"],
                "summary": "Engineering principles for designing products that are easy and cost-effective to manufacture and assemble.",
                "content": """
<h2>Design for Manufacturing & Assembly (DFM/DFA)</h2>
<p>DFM and DFA are systematic approaches to designing products so they can be manufactured and assembled at the lowest cost with the highest quality. Research shows that 70-80% of a product's manufacturing cost is determined at the design stage, making design the highest-leverage point for cost reduction.</p>

<h3>DFM Principles</h3>
<ol>
<li><strong>Minimize part count:</strong> Combine functions. Fewer parts = fewer operations, fixtures, suppliers, and failure modes. Ask: Does this part move relative to adjacent parts? Must it be a different material? Must it be separate for assembly?</li>
<li><strong>Design for ease of fabrication:</strong> Use standard processes, avoid tight tolerances unless functionally required, design for the most capable manufacturing process.</li>
<li><strong>Minimize assembly directions:</strong> Design for top-down (Z-axis) assembly to leverage gravity and simplify fixturing.</li>
<li><strong>Maximize compliance:</strong> Design parts with lead-in chamfers, generous tolerances, and self-aligning features to accommodate assembly variation.</li>
<li><strong>Minimize handling:</strong> Avoid parts that tangle, nest, stick, are slippery, or are too small/large to grip. Design parts that are symmetric or obviously asymmetric (avoid near-symmetry).</li>
<li><strong>Use standard components:</strong> Standard fasteners, bearings, connectors, and materials reduce cost, improve availability, and simplify procurement.</li>
<li><strong>Design for part symmetry:</strong> If a part can be symmetric, make it so. If it must be asymmetric, make it obviously so — not nearly symmetric.</li>
<li><strong>Eliminate secondary operations:</strong> Avoid post-processing (deburring, painting, plating) through design choices. Use materials that don't require finishing.</li>
<li><strong>Design for testability:</strong> Build in test points, self-diagnostic features, and accessibility for inspection.</li>
</ol>

<h3>Pugh Matrix (Concept Selection)</h3>
<p>A systematic method for evaluating and selecting the best design concept against multiple criteria. Compare all alternatives against a baseline (datum) using +, -, or S (same) scoring for each criterion. Weight criteria by importance. The concept with the highest net score is selected for further development.</p>
"""
            }
        ]
    },
    {
        "id": "metrics",
        "title": "KPIs & Metrics",
        "icon": "metrics",
        "topics": [
            {
                "id": "manufacturing-kpis",
                "title": "Manufacturing KPIs",
                "tags": ["OEE", "FPY", "OTIF"],
                "summary": "Comprehensive guide to key performance indicators used to measure manufacturing excellence.",
                "content": """
<h2>Manufacturing KPIs</h2>
<p>Key Performance Indicators (KPIs) are quantifiable measures that reflect the critical success factors of manufacturing operations. Effective KPIs follow the SMART criteria: Specific, Measurable, Achievable, Relevant, and Time-bound.</p>

<h3>SQDC(M) KPI Framework</h3>

<h4>Safety KPIs</h4>
<table>
<tr><th>KPI</th><th>Formula</th><th>World-Class Target</th></tr>
<tr><td>LTIR (Lost Time Incident Rate)</td><td>(Lost-time incidents × 200,000) / Total hours worked</td><td><0.5</td></tr>
<tr><td>TRIR (Total Recordable Incident Rate)</td><td>(Recordable incidents × 200,000) / Total hours worked</td><td><1.0</td></tr>
<tr><td>Near-Miss Reporting Rate</td><td>Near-misses reported per 100 employees per month</td><td>>10 (high reporting = strong safety culture)</td></tr>
<tr><td>Safety Audit Completion Rate</td><td>Audits completed / Audits planned × 100</td><td>100%</td></tr>
</table>

<h4>Quality KPIs</h4>
<table>
<tr><th>KPI</th><th>Formula</th><th>World-Class Target</th></tr>
<tr><td>First Pass Yield (FPY)</td><td>Good units from first attempt / Total units started × 100</td><td>≥99%</td></tr>
<tr><td>Rolled Throughput Yield (RTY)</td><td>FPY₁ × FPY₂ × ... × FPYₙ (product of all process step yields)</td><td>≥95%</td></tr>
<tr><td>PPM (Parts Per Million) Defective</td><td>(Defective units / Total units) × 1,000,000</td><td><50 PPM</td></tr>
<tr><td>COPQ (Cost of Poor Quality)</td><td>Internal failure + External failure + Appraisal + Prevention costs</td><td><3% of revenue</td></tr>
<tr><td>Scrap Rate</td><td>Scrapped units or material value / Total production</td><td><1%</td></tr>
<tr><td>Rework Rate</td><td>Units requiring rework / Total units produced × 100</td><td><2%</td></tr>
</table>

<h4>Delivery KPIs</h4>
<table>
<tr><th>KPI</th><th>Formula</th><th>World-Class Target</th></tr>
<tr><td>OTIF (On Time In Full)</td><td>Orders delivered on time AND in full / Total orders × 100</td><td>≥98%</td></tr>
<tr><td>Schedule Adherence</td><td>Units produced per schedule / Units planned × 100</td><td>≥95%</td></tr>
<tr><td>Manufacturing Lead Time</td><td>Time from order release to completion (door-to-door)</td><td>Industry-specific; target reduction</td></tr>
<tr><td>Order-to-Delivery Lead Time</td><td>Time from customer order to delivery</td><td>Continuously reduce</td></tr>
</table>

<h4>Cost / Productivity KPIs</h4>
<table>
<tr><th>KPI</th><th>Formula</th><th>World-Class Target</th></tr>
<tr><td>OEE</td><td>Availability × Performance × Quality</td><td>≥85%</td></tr>
<tr><td>TEEP (Total Effective Equipment Performance)</td><td>OEE × Utilization (where Utilization = Scheduled Time / Calendar Time)</td><td>Varies; measures total asset utilization</td></tr>
<tr><td>Labor Productivity</td><td>Units produced / Direct labor hours</td><td>Year-over-year improvement</td></tr>
<tr><td>Material Yield</td><td>Finished product output / Raw material input × 100</td><td>≥95% (varies by process)</td></tr>
<tr><td>Inventory Turns</td><td>COGS / Average inventory</td><td>≥12 (monthly turns)</td></tr>
<tr><td>Energy per Unit</td><td>Energy consumed (kWh) / Units produced</td><td>Continuously reduce</td></tr>
</table>

<h4>Morale KPIs</h4>
<table>
<tr><th>KPI</th><th>Formula</th><th>World-Class Target</th></tr>
<tr><td>Absenteeism Rate</td><td>Absent days / Available work days × 100</td><td><3%</td></tr>
<tr><td>Employee Turnover</td><td>Employees leaving / Average headcount × 100 (annual)</td><td><10%</td></tr>
<tr><td>Suggestion Rate</td><td>Improvement suggestions per employee per year</td><td>≥12 (1/month)</td></tr>
<tr><td>Skill Matrix Completion</td><td>Certified skills / Required skills × 100</td><td>≥80%</td></tr>
<tr><td>Training Hours</td><td>Training hours per employee per year</td><td>≥40 hours</td></tr>
</table>
"""
            }
        ]
    },
    {
        "id": "culture",
        "title": "Culture & People",
        "icon": "people",
        "topics": [
            {
                "id": "lean-culture",
                "title": "Building a Lean Culture",
                "tags": ["Culture", "Leadership", "Respect"],
                "summary": "Developing the mindset, behaviors, and leadership practices that sustain manufacturing excellence.",
                "content": """
<h2>Building a Lean Culture</h2>
<p>Tools and techniques account for perhaps 20% of a Lean transformation's success. The remaining 80% comes from culture — the shared beliefs, behaviors, and norms that determine how people think, decide, and act every day. Building a Lean culture requires a fundamental shift in leadership behavior and organizational values.</p>

<h3>The Two Pillars of Lean Culture</h3>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Pillar 1</span><h4>Continuous Improvement (Kaizen)</h4></div>
<p>Every person, every day, everywhere is looking for ways to improve. Improvement is not an event or a project — it is a habit. The standard is never good enough. Problems are opportunities, not failures. Data drives decisions, not opinions or hierarchy.</p>
</div>

<div class="concept-box">
<div class="concept-box-header"><span class="concept-box-label">Pillar 2</span><h4>Respect for People</h4></div>
<p>Respecting people means developing their capabilities, valuing their ideas, and challenging them to grow. It does NOT mean being "nice" or avoiding difficult conversations. True respect is investing in people's development, giving them the tools and authority to improve their own work, and holding them accountable to standards. Operators closest to the work often have the best ideas.</p>
</div>

<h3>Leadership Behaviors for Lean Culture</h3>
<ol>
<li><strong>Go to Gemba daily:</strong> Spend time on the shop floor observing, asking questions, and coaching. Decision-making authority should be as close to the work as possible.</li>
<li><strong>Ask questions, don't give answers:</strong> "What do you think?" "What did you try?" "What happened?" "What will you do next?" Leaders develop problem-solvers, not followers.</li>
<li><strong>Make problems visible:</strong> Create an environment where exposing problems is celebrated, not punished. The worst thing in a Lean culture is a hidden problem.</li>
<li><strong>Model the behavior:</strong> Leaders must personally practice 5S, follow standardized work, participate in Kaizen events, and demonstrate respect for people in every interaction.</li>
<li><strong>Focus on process, not results:</strong> Results are outcomes of good processes. If you get good results from a bad process, you got lucky. If you get bad results from a good process, investigate and learn.</li>
<li><strong>Think long-term:</strong> Invest in people development, process improvement, and culture building even when short-term pressures push for shortcuts.</li>
</ol>

<h3>Hansei (Reflection)</h3>
<p>Hansei (反省) is the practice of honest self-reflection — acknowledging what went wrong and committing to improvement. In Japanese culture, Hansei is not about blame but about taking responsibility and learning. In manufacturing, Hansei is practiced through:</p>
<ul>
<li>Post-project reviews (What went well? What didn't? What will we do differently?)</li>
<li>End-of-day reflection by leaders</li>
<li>Yokoten (横展) — horizontal deployment of lessons learned across the organization</li>
</ul>

<h3>Skill Matrix & People Development</h3>
<p>A visual matrix showing each operator's skill level across all required tasks. Typically uses a 4-level system:</p>
<table>
<tr><th>Level</th><th>Symbol</th><th>Description</th></tr>
<tr><td>1</td><td>Quarter circle</td><td>Under training — can perform with supervision</td></tr>
<tr><td>2</td><td>Half circle</td><td>Can perform independently to standard</td></tr>
<tr><td>3</td><td>Three-quarter circle</td><td>Can perform and train others</td></tr>
<tr><td>4</td><td>Full circle</td><td>Can improve the process — problem-solver and innovator</td></tr>
</table>
<p>Target: every workstation has at least 3 operators at Level 2 or above. The skill matrix drives training plans, job rotation schedules, and succession planning.</p>
"""
            },
            {
                "id": "change-management",
                "title": "Change Management in Manufacturing",
                "tags": ["Change", "Resistance", "Adoption"],
                "summary": "Frameworks and strategies for leading successful manufacturing transformation programs.",
                "content": """
<h2>Change Management in Manufacturing</h2>
<p>Manufacturing transformations fail not because of technical shortcomings but because of people. Change management in manufacturing must address shop floor realities: shift workers, union dynamics, decades of ingrained habits, and skepticism born from previous failed initiatives ("flavor of the month").</p>

<h3>Kotter's 8-Step Change Model (Manufacturing Context)</h3>
<div class="process-steps">
<div class="process-step"><div class="step-number">1</div><div class="step-content"><h5>Create Urgency</h5><p>Share competitive data, customer complaints, cost benchmarks. Take managers to benchmark plants. Make the burning platform tangible. "If we don't change, we will lose this contract to a competitor who delivers in 3 days while we take 14."</p></div></div>
<div class="process-step"><div class="step-number">2</div><div class="step-content"><h5>Build a Guiding Coalition</h5><p>Identify respected informal leaders on the shop floor — not just management. Include experienced operators, union stewards, and skilled technicians who others look to for credibility.</p></div></div>
<div class="process-step"><div class="step-number">3</div><div class="step-content"><h5>Form a Strategic Vision</h5><p>Define the future state in concrete, shop-floor terms. Not "world-class manufacturing" but "a workplace where every operator has the tools, training, and authority to stop and fix problems immediately."</p></div></div>
<div class="process-step"><div class="step-number">4</div><div class="step-content"><h5>Enlist a Volunteer Army</h5><p>Train Kaizen champions on every shift. Start with willing early adopters. Let skeptics observe success before pressuring them to participate.</p></div></div>
<div class="process-step"><div class="step-number">5</div><div class="step-content"><h5>Enable Action by Removing Barriers</h5><p>Remove bureaucratic approval processes for small improvements. Provide Kaizen budgets for teams. Address managers who undermine changes.</p></div></div>
<div class="process-step"><div class="step-number">6</div><div class="step-content"><h5>Generate Short-Term Wins</h5><p>Start with 5S in a pilot area — visible results in days. Run a SMED event to cut changeover time in half. Show measurable improvement within the first 30-60 days.</p></div></div>
<div class="process-step"><div class="step-number">7</div><div class="step-content"><h5>Sustain Acceleration</h5><p>Expand from pilot to plant-wide. Train more Kaizen leaders. Build improvement into KPIs and reviews. Don't declare victory after one success.</p></div></div>
<div class="process-step"><div class="step-number">8</div><div class="step-content"><h5>Institute Change</h5><p>Embed improvements into SOPs, training programs, and the management system (DWM). New hires learn the Lean way from day one. It becomes "how we do things here."</p></div></div>
</div>

<h3>Common Resistance Patterns</h3>
<table>
<tr><th>Resistance</th><th>Root Cause</th><th>Response</th></tr>
<tr><td>"We tried this before"</td><td>Failed past initiatives</td><td>Acknowledge the past. Explain what's different this time. Start small and prove it.</td></tr>
<tr><td>"This is just another management fad"</td><td>Lack of sustained leadership commitment</td><td>Leaders must be visibly committed for months/years, not just at the launch event.</td></tr>
<tr><td>"I'll lose my job if we eliminate waste"</td><td>Fear of displacement</td><td>Commit to no layoffs from improvement. Redeploy freed capacity to growth or improvement work.</td></tr>
<tr><td>"You don't understand our process"</td><td>Expertise pride / outsider skepticism</td><td>Involve operators in the analysis. Respect their knowledge. Build solutions with them, not for them.</td></tr>
<tr><td>"We don't have time for this"</td><td>Overwhelmed with firefighting</td><td>The improvements will reduce firefighting. Start with small, quick wins that free up time.</td></tr>
</table>
"""
            }
        ]
    }
]


def icon_svg(icon_type):
    icons = {
        "foundation": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18M3 10h18M5 6l7-3 7 3M4 10v11M8 10v11M12 10v11M16 10v11M20 10v11"/></svg>',
        "tools": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>',
        "quality": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
        "strategy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg>',
        "advanced": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>',
        "metrics": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
        "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>',
    }
    return icons.get(icon_type, icons["tools"])


def nav_item_icon_svg():
    return '<svg class="nav-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/></svg>'


def build_sidebar_nav(cats):
    html = ""
    for cat in cats:
        html += f'''<div class="nav-section">
  <div class="nav-section-header" onclick="toggleSection(this)">
    <span class="nav-section-title">{cat["title"]}</span>
    <svg class="nav-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
  </div>
  <div class="nav-group">\n'''
        for topic in cat["topics"]:
            html += f'    <a class="nav-item" data-section="{topic["id"]}" onclick="navigate(\'{topic["id"]}\')">{nav_item_icon_svg()}<span>{topic["title"]}</span></a>\n'
        html += "  </div>\n</div>\n"
    return html


def build_overview_cards(cats):
    all_topics = []
    for cat in cats:
        for t in cat["topics"]:
            all_topics.append(t)
    cards_html = ""
    for t in all_topics:
        tags_html = "".join(f'<span class="tag">{tag}</span>' for tag in t["tags"])
        cards_html += f'''<div class="topic-card" onclick="navigate('{t["id"]}')">
  <div class="topic-card-header">
    <div class="topic-card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2z"/><path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/></svg></div>
    <div><h3>{t["title"]}</h3></div>
  </div>
  <p>{t["summary"]}</p>
  <div class="topic-card-tags">{tags_html}</div>
</div>\n'''
    return cards_html


def build_sections(cats):
    html = ""
    for cat in cats:
        for t in cat["topics"]:
            html += f'''<div class="section" id="section-{t["id"]}">
  <button class="back-to-category" onclick="navigate('home')">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
    Back to Overview
  </button>
  <div class="article">
    {t["content"]}
  </div>
</div>\n'''
    return html


# Count topics
total_topics = sum(len(c["topics"]) for c in categories)
total_categories = len(categories)

# Build HTML
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Manufacturing Excellence Knowledge Base</title>
  <meta name="description" content="Comprehensive reference guide covering all terms, tools, and methods of manufacturing excellence — Lean, Six Sigma, TPM, TPS, and more.">
  <link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@400,500,700,800&f[]=satoshi@300,400,500,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./base.css">
  <link rel="stylesheet" href="./style.css">
</head>
<body>
<div class="app">

  <!-- Sidebar -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-logo">
        <svg viewBox="0 0 32 32" fill="none">
          <rect x="2" y="2" width="28" height="28" rx="6" stroke="currentColor" stroke-width="2" fill="none" style="color: var(--color-primary)"/>
          <path d="M8 22V14l8-6 8 6v8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--sidebar-text-active)"/>
          <path d="M13 22v-5h6v5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--sidebar-text-active)"/>
          <circle cx="16" cy="14" r="2" fill="currentColor" style="color: var(--color-primary)"/>
        </svg>
        <div>
          <div class="sidebar-logo-text">MFG Excellence</div>
          <div class="sidebar-logo-sub">Knowledge Base</div>
        </div>
      </div>
    </div>

    <div class="sidebar-search">
      <div class="sidebar-search-wrapper">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="searchInput" placeholder="Search topics..." oninput="filterNav(this.value)">
      </div>
    </div>

    <nav class="sidebar-nav" id="sidebarNav">
      <div class="nav-section">
        <a class="nav-item active" data-section="home" onclick="navigate('home')">
          <svg class="nav-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          <span>Overview</span>
        </a>
      </div>
      {build_sidebar_nav(categories)}
    </nav>
  </aside>

  <!-- Overlay for mobile -->
  <div class="sidebar-overlay" id="sidebarOverlay" onclick="closeSidebar()"></div>

  <!-- Main Content -->
  <main class="main">
    <header class="topbar">
      <div class="topbar-left">
        <nav class="breadcrumb">
          <span>MFG Excellence</span>
          <span class="breadcrumb-sep">/</span>
          <span class="breadcrumb-current" id="breadcrumbCurrent">Overview</span>
        </nav>
      </div>
      <div class="topbar-actions">
        <button class="btn-icon" data-theme-toggle aria-label="Toggle dark mode">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
        </button>
      </div>
    </header>

    <div class="content-area">
      <!-- HOME / OVERVIEW -->
      <div class="section active" id="section-home">
        <div class="hero">
          <h1>Manufacturing Excellence Knowledge Base</h1>
          <p>A comprehensive reference covering every major term, tool, methodology, and framework in manufacturing excellence — from Lean and Six Sigma to TPM, Hoshin Kanri, and Industry 4.0. Built for consultants, engineers, and leaders driving operational transformation.</p>
          <div class="hero-stats">
            <div class="hero-stat">
              <span class="hero-stat-value">{total_topics}</span>
              <span class="hero-stat-label">Topics</span>
            </div>
            <div class="hero-stat">
              <span class="hero-stat-value">{total_categories}</span>
              <span class="hero-stat-label">Categories</span>
            </div>
            <div class="hero-stat">
              <span class="hero-stat-value">50+</span>
              <span class="hero-stat-label">Methods & Tools</span>
            </div>
          </div>
        </div>

        <div class="topic-grid">
          {build_overview_cards(categories)}
        </div>
      </div>

      <!-- TOPIC SECTIONS -->
      {build_sections(categories)}
    </div>
  </main>
</div>

<!-- Mobile Toggle -->
<button class="mobile-toggle" onclick="toggleSidebar()" aria-label="Toggle navigation">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
</button>

<script>
// Dark mode toggle
(function () {{
  const t = document.querySelector('[data-theme-toggle]'),
    r = document.documentElement;
  let d = matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light';
  r.setAttribute('data-theme', d);
  t &&
    t.addEventListener('click', () => {{
      d = d === 'dark' ? 'light' : 'dark';
      r.setAttribute('data-theme', d);
      t.setAttribute('aria-label', 'Switch to ' + (d === 'dark' ? 'light' : 'dark') + ' mode');
      t.innerHTML =
        d === 'dark'
          ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>'
          : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
    }});
}})();

// Navigation
function navigate(sectionId) {{
  document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
  const target = document.getElementById('section-' + sectionId);
  if (target) target.classList.add('active');

  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  const navItem = document.querySelector('.nav-item[data-section="' + sectionId + '"]');
  if (navItem) {{
    navItem.classList.add('active');
    navItem.scrollIntoView({{ block: 'nearest' }});
  }}

  // Update breadcrumb
  const bc = document.getElementById('breadcrumbCurrent');
  if (sectionId === 'home') {{
    bc.textContent = 'Overview';
  }} else if (navItem) {{
    bc.textContent = navItem.querySelector('span').textContent;
  }}

  // Scroll to top
  document.querySelector('.content-area').scrollTop = 0;
  window.scrollTo(0, 0);

  // Close mobile sidebar
  closeSidebar();
}}

// Sidebar toggle (mobile)
function toggleSidebar() {{
  document.getElementById('sidebar').classList.toggle('open');
  document.getElementById('sidebarOverlay').classList.toggle('show');
}}
function closeSidebar() {{
  document.getElementById('sidebar').classList.remove('open');
  document.getElementById('sidebarOverlay').classList.remove('show');
}}

// Section collapse/expand
function toggleSection(header) {{
  header.classList.toggle('collapsed');
  const group = header.nextElementSibling;
  if (group.classList.contains('collapsed')) {{
    group.classList.remove('collapsed');
    group.style.maxHeight = group.scrollHeight + 'px';
  }} else {{
    group.style.maxHeight = group.scrollHeight + 'px';
    requestAnimationFrame(() => {{
      group.classList.add('collapsed');
    }});
  }}
}}

// Initialize nav group heights
document.querySelectorAll('.nav-group').forEach(g => {{
  g.style.maxHeight = g.scrollHeight + 'px';
}});

// Search / filter
function filterNav(query) {{
  query = query.toLowerCase().trim();
  document.querySelectorAll('.nav-item[data-section]').forEach(item => {{
    if (item.dataset.section === 'home') return;
    const text = item.querySelector('span').textContent.toLowerCase();
    item.style.display = (!query || text.includes(query)) ? '' : 'none';
  }});
  // Show all sections if query
  if (query) {{
    document.querySelectorAll('.nav-group').forEach(g => {{
      g.classList.remove('collapsed');
      g.style.maxHeight = g.scrollHeight + 'px';
    }});
    document.querySelectorAll('.nav-section-header').forEach(h => h.classList.remove('collapsed'));
  }}
}}

// Keyboard shortcut: / to focus search
document.addEventListener('keydown', (e) => {{
  if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {{
    e.preventDefault();
    document.getElementById('searchInput').focus();
  }}
}});
</script>
</body>
</html>'''

with open('/home/user/workspace/mfg-excellence-kb/index.html', 'w') as f:
    f.write(html)

print(f"Generated index.html with {total_topics} topics across {total_categories} categories")
print(f"File size: {len(html)} characters")
