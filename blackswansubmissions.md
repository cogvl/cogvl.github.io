---
layout: default
title: BlackSwan Challenge — Submission Details
description: Submission guidelines and evaluation details for the BlackSwan Challenge at CogVL CVPR 2026.
permalink: /blackswansubmissions/
---

<div class="challenge-hero">
    <div class="container">
        <h1>BlackSwan Challenge</h1>
        <p style="font-size: 1.25rem; margin-top: 1rem;">Submission Details &amp; Evaluation Guidelines</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="section-content">
            <p style="font-size: 0.9rem; color: var(--text-light);">
                <strong>Black Swan: Abductive and Defeasible Video Reasoning in Unpredictable Events</strong><br>
                Aditya Chinchure<sup>1,2*</sup>, Sahithya Ravi<sup>1,2*</sup>, Raymond Ng<sup>1</sup>, Vered Shwartz<sup>1,2</sup>, Boyang Li<sup>3</sup>, Leonid Sigal<sup>1,2</sup><br>
                <sup>1</sup>University of British Columbia, <sup>2</sup>Vector Institute for AI, <sup>3</sup>Nanyang Technological University
            </p>

            <h2>About the Dataset</h2>
            <p><strong>BlackSwan</strong> is a benchmark for evaluating VLMs' ability to reason about unexpected events through abductive and defeasible tasks. Our tasks artificially limit the amount of visual information provided to models while questioning them about hidden unexpected events, or provide new visual information that could change an existing hypothesis.</p>

            <p><strong>We release our data with two splits:</strong></p>
            <ul style="margin-left: 1.5rem; margin-bottom: var(--spacing-sm);">
                <li><strong>Validation Split:</strong> Ground truth labels are accessible for model development.</li>
                <li><strong>Test Split:</strong> Ground truth labels are hidden; email your predictions to the organizers for evaluation.</li>
            </ul>
            <p>We encourage participants to use the validation split during development and submit a final model version for test set evaluation. The validation set contains <strong>827 videos</strong> (50% of data) and the test set contains <strong>828 videos</strong>, making it slightly more challenging. Overall, the dataset comprises over <strong>3,800 MCQ tasks</strong> spanning <strong>1,655 videos</strong>. The challenge evaluates MCQ tasks only.</p>

            <div class="challenge-links" style="justify-content: flex-start; margin: var(--spacing-md) 0;">
                <a href="https://huggingface.co/collections/UBC-ViL/black-swan-abductive-and-defeasible-reasoning-67de1a4ab7ddc22edf0b0542"
                   target="_blank" rel="noopener noreferrer" class="btn">
                    <i class="fas fa-download"></i> Access the Dataset
                </a>
                <a href="{{ '/blackswanchallenge/' | relative_url }}" class="btn btn-secondary">
                    <i class="fas fa-arrow-left"></i> Back to Challenge
                </a>
            </div>
        </div>
    </div>
</section>

<section class="section" style="background-color: var(--bg-light);">
    <div class="container">
        <div class="section-content">
            <h2>Evaluation</h2>
            <p>We evaluate model performance using <strong>accuracy</strong> — the proportion of correctly answered MCQ questions. In addition to overall accuracy, we report per-subtask scores to provide deeper insights into model reasoning capabilities.</p>

            <div class="topics-grid">
                <div class="topic-card">
                    <h3><i class="fas fa-search"></i> Detective Score</h3>
                    <p>Questions where only the pre-event and post-event clips are provided as context. Tests <strong>abductive reasoning</strong> — inferring the hidden cause of an unexpected event.</p>
                </div>
                <div class="topic-card">
                    <h3><i class="fas fa-sync-alt"></i> Reporter Score</h3>
                    <p>Questions where the entire video is provided as context. Tests <strong>defeasible reasoning</strong> — revising a hypothesis when new visual evidence appears.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-content">
            <h2>Submission Guidelines</h2>

            <div class="highlight-box">
                <h3><i class="fas fa-envelope" style="margin-right: 0.5rem;"></i> How to Submit</h3>
                <p>Email your predictions to the organizers at <strong><a href="mailto:cogvl2026@googlegroups.com">cogvl2026@googlegroups.com</a></strong> with the subject line:</p>
                <div style="background: var(--bg-color); border: 1px solid var(--border-color); border-radius: var(--border-radius); padding: var(--spacing-sm); font-family: monospace; margin: var(--spacing-sm) 0;">
                    BlackSwan Challenge Submission — [Team Name]
                </div>
                <p style="margin-bottom: 0;">Please include in the email body: your team name, affiliation, a brief description of your approach, and attach the JSON prediction file described below. The organizers will evaluate your submission and reply with your overall accuracy, Detective score, and Reporter score.</p>
            </div>

            <h3>MCQ Prediction File Format</h3>
            <p>Attach a <strong>JSON file</strong> to your email where each key is a question ID (string) and each value is the index of the selected MCQ option (0-indexed integer).</p>
            <p>Example:</p>
            <div style="background: var(--bg-light); border: 1px solid var(--border-color); padding: var(--spacing-sm); border-radius: var(--border-radius); font-family: monospace; overflow-x: auto;">
                {<br>
                &nbsp;&nbsp;"0": 0,<br>
                &nbsp;&nbsp;"1": 0,<br>
                &nbsp;&nbsp;"2": 1,<br>
                &nbsp;&nbsp;"3": 0,<br>
                &nbsp;&nbsp;"4": 1,<br>
                &nbsp;&nbsp;"5": 1<br>
                }
            </div>
        </div>
    </div>
</section>

<section class="section" style="background-color: var(--bg-light);">
    <div class="container">
        <div class="section-content">
            <h2>Terms and Conditions</h2>
            <p>By accessing, downloading, or using our data, you acknowledge that the BlackSwan team does not own the copyright to these videos and that they are solely provided for non-commercial research and/or educational purposes. This dataset is licensed under a <strong><a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a></strong>.</p>

            <h3>BibTeX Citation</h3>
            <p>To cite the BlackSwan dataset, please use:</p>
            <div style="background: var(--bg-color); border: 1px solid var(--border-color); padding: var(--spacing-sm); border-radius: var(--border-radius); font-family: monospace; overflow-x: auto;">
                @misc{chinchure2024blackswanabductivedefeasible,<br>
                &nbsp;&nbsp;title={Black Swan: Abductive and Defeasible Video Reasoning in Unpredictable Events},<br>
                &nbsp;&nbsp;author={Aditya Chinchure and Sahithya Ravi and Raymond Ng and Vered Shwartz and Boyang Li and Leonid Sigal},<br>
                &nbsp;&nbsp;year={2024},<br>
                &nbsp;&nbsp;eprint={2412.05725},<br>
                &nbsp;&nbsp;archivePrefix={arXiv},<br>
                &nbsp;&nbsp;primaryClass={cs.CV},<br>
                &nbsp;&nbsp;url={https://arxiv.org/abs/2412.05725}<br>
                }
            </div>
        </div>
    </div>
</section>