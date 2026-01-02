---
layout: default
title: BlackSwan Challenge
description: The BlackSwan Challenge evaluates abductive and defeasible reasoning capabilities of VLMs in unexpected video events.
permalink: /blackswanchallenge/
---

<div class="challenge-hero">
    <div class="container">
        <h1>The 1st BlackSwan Challenge</h1>
        <p style="font-size: 1.25rem; margin-top: 1rem;">Evaluating Abductive and Defeasible Reasoning in Unpredictable Events</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="section-content">
            <h2>Overview</h2>
            <p>We feature the BlackSwan Challenge based on our dataset presented at CVPR 2025, which measures deeper reasoning abilities of VLMs in unforeseen and unexpected scenarios.</p>
            
            <div class="challenge-figure">
                <img src="{{ '/static/images/VARmain.png' | relative_url }}" alt="BlackSwan Dataset Tasks">
                <p style="margin-top: 1rem; color: var(--text-light); font-size: 0.9rem;">
                    The BlackSwan dataset features three tasks: Forecaster (evaluating what happens next), Detective (testing abductive reasoning) and Reporter (testing defeasible reasoning). Our challenge tests Video-VLMs capabilities at these challenging tasks on unexpected and surprising events in videos.
                </p>
            </div>
        </div>
    </div>
</section>

<section class="section" style="background-color: var(--bg-light);">
    <div class="container">
        <div class="section-content">
            <h2 class="text-center">Get Started</h2>
            <div class="challenge-links">
                <a href="https://blackswan.cs.ubc.ca" target="_blank" rel="noopener noreferrer" class="btn">
                    <i class="fas fa-globe"></i> Visit BlackSwan Website
                </a>
                <a href="https://huggingface.co/collections/UBC-ViL/black-swan-abductive-and-defeasible-reasoning" target="_blank" rel="noopener noreferrer" class="btn">
                    <i class="fas fa-download"></i> Download Dataset
                </a>
                <a href="https://eval.ai/web/challenges/challenge-page/2484/leaderboard" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">
                    <i class="fas fa-trophy"></i> View Leaderboard
                </a>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="highlight-box">
            <h3>Challenge Timeline</h3>
            <ul class="timeline">
                <li class="timeline-item">
                    <span class="timeline-date">January 2026</span> - Challenge Launch
                </li>
                <li class="timeline-item">
                    <span class="timeline-date">End of April 2026</span> - Challenge Closes
                </li>
            </ul>
        </div>
    </div>
</section>

<section class="section" style="background-color: var(--bg-light);">
    <div class="container">
        <div class="section-content">
            <h2>Background</h2>
            <p>The BlackSwan Challenge arises from the need to rigorously evaluate the abductive and defeasible reasoning capabilities of modern vision-language models (VLMs) in video understanding. While large-scale multimodal models have achieved impressive performance on typical visual reasoning benchmarks, often excelling at describing and interpreting everyday events, their reasoning is frequently correlational rather than cognitive. Existing datasets overwhelmingly emphasize common, well-structured scenarios, leaving it unclear whether VLMs genuinely infer causal explanations or merely rely on memorized statistical patterns.</p>
            
            <p>In contrast, reasoning about unexpected or out-of-distribution events (the "black swan" events of the real world) requires models to move beyond perception and recall, and employ higher-order cognitive reasoning processes. In humans, such reasoning involves abduction (inferring the most plausible hidden cause behind an observation) and defeasibility (updating one's hypothesis when new, conflicting evidence appears). Building models with these abilities is essential for robust, human-like understanding of dynamic real-world environments.</p>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-content">
            <h2>The Challenge</h2>
            <p>To this end, we introduce the BlackSwan Challenge, built upon the recently developed BlackSwanSuite benchmark presented at CVPR 2025. The benchmark evaluates how well VLMs can reason about unexpected events in videos through a set of multiple-choice (MCQ) and yes/no (Y/N) questions. Each question type targets a distinct reasoning skill:</p>
            
            <div class="topics-grid">
                <div class="topic-card">
                    <h3><i class="fas fa-search"></i> Abductive Reasoning</h3>
                    <p>Tasks probe models' ability to infer hidden or missing causes behind surprising events when only partial visual information is provided.</p>
                </div>
                
                <div class="topic-card">
                    <h3><i class="fas fa-sync-alt"></i> Defeasible Reasoning</h3>
                    <p>Tasks assess whether models can revise their previous conclusions when presented with new evidence that contradicts their earlier assumptions.</p>
                </div>
            </div>
            
            <p>The dataset comprises over <strong>3,800 MCQ</strong>, <strong>4,900 generative</strong>, and <strong>6,700 Y/N tasks</strong> across <strong>1,655 videos</strong>, each containing atypical, counterintuitive, or unexpected visual situations. These scenarios are deliberately constructed to minimize the usefulness of memorized patterns, forcing models to reason instead of recall. BlackSwan is challenging for VLMs, with significant performance gaps of up to <strong>32%</strong> from humans on these tasks.</p>
        </div>
    </div>
</section>

<section class="section" style="background-color: var(--bg-light);">
    <div class="container">
        <div class="section-content">
            <h2>Connection to Workshop Goals</h2>
            <p>The BlackSwan Challenge aligns closely with the mission of CogVL, which seeks to reintroduce and evaluate human cognitive principles such as causal inference, theory of mind, and counterfactual reasoning in multimodal learning. BlackSwan tests the abductive and defeasible reasoning capabilities of multimodal models under uncertainty. The challenge directly probes the cognitive depth of VLMs and exposes their current limitations in handling non-canonical, unexpected, and dynamic events. Through this challenge, we aim to stimulate research into VLM architectures, training, and inference-time methods that advance video understanding models toward robust, interpretable, and cognitively grounded reasoning.</p>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-content">
            <h2>Evaluation</h2>
            <p>Submissions to the BlackSwan Challenge will be evaluated on EvalAI using accuracy as the evaluation metric for both MCQ and Y/N tasks. BlackSwanSuite is divided into a public validation set and a private test set, which prevents overfitting. Participants will have access to videos and questions from the public validation set and the private test set. The validation set will have its ground-truth answers available, whereas the test set answers are private.</p>
            
            <p>Videos will be provided with the Creative Commons Attribution Non Commercial Share Alike 4.0 license. Challenge results will use test set scores, which will only be computed using the leaderboard. Participants must submit a JSON file containing their model's predictions for their test set. The leaderboard will enable comparison with human baselines and state-of-the-art VLMs such as GPT-4o and LLaVA-Video.</p>
        </div>
    </div>
</section>



