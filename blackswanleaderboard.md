---
layout: default
title: BlackSwan Challenge — Leaderboard
description: Leaderboard for the BlackSwan Challenge at CogVL CVPR 2026, showing accuracy scores for Detective and Reporter tasks.
permalink: /blackswanleaderboard/
---

<div class="challenge-hero">
    <div class="container">
        <h1>BlackSwan Challenge Leaderboard</h1>
        <p style="font-size: 1.25rem; margin-top: 1rem;">MCQ Test Phase — MCQ Test Split</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="section-content">
            <h2>Results</h2>
            <p>The leaderboard shows Accuracy (overall), as well as accuracy of MCQ and YN variants of Detective and Reporter tasks separately. For human baseline, please refer to our paper.</p>

            <div class="leaderboard-legend">
                <span class="baseline-badge">B</span> Baseline
                <span style="margin-left: 1.5rem;"></span>
                <span class="participant-badge">P</span> Participant
            </div>

            <div class="leaderboard-wrapper">
                <table class="leaderboard-table">
                    <thead>
                        <tr>
                            <th>Rank</th>
                            <th>Team</th>
                            <th>Accuracy</th>
                            <th>Detective_Accuracy</th>
                            <th>Reporter_Accuracy</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="participant-row">
                            <td>1</td>
                            <td>cola_lover (v1) (Anonymous Affiliation) <span class="participant-badge">P</span></td>
                            <td>75.94</td>
                            <td>72.33</td>
                            <td>81.75</td>
                        </tr>
                        <tr class="participant-row">
                            <td>2</td>
                            <td>Boat (v1) (Jiangnan University) <span class="participant-badge">P</span></td>
                            <td>72.88</td>
                            <td>67.78</td>
                            <td>81.11</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td>UBC-ViL (Baseline-GPT4o) <span class="baseline-badge">B</span></td>
                            <td>69.06</td>
                            <td>63.18</td>
                            <td>78.53</td>
                        </tr>
                        <tr>
                            <td>4</td>
                            <td>IMG_AI</td>
                            <td>64.17</td>
                            <td>56.86</td>
                            <td>75.96</td>
                        </tr>
                        <tr>
                            <td>5</td>
                            <td>UBC-ViL (Baseline-Gemini) <span class="baseline-badge">B</span></td>
                            <td>62.20</td>
                            <td>57.09</td>
                            <td>70.60</td>
                        </tr>
                        <tr class="participant-row">
                            <td>6</td>
                            <td>ASU_Computer_Vision (v2) <span class="participant-badge">P</span></td>
                            <td>62.06</td>
                            <td>56.22</td>
                            <td>71.47</td>
                        </tr>
                        <tr>
                            <td>7</td>
                            <td>UBC-ViL (Baseline-LlavaVideo) <span class="baseline-badge">B</span></td>
                            <td>60.63</td>
                            <td>54.55</td>
                            <td>70.44</td>
                        </tr>
                        <tr>
                            <td>8</td>
                            <td>casia-base</td>
                            <td>59.94</td>
                            <td>52.07</td>
                            <td>72.62</td>
                        </tr>
                        <tr>
                            <td>9</td>
                            <td>UBC-ViL (Baseline-VideoLlama2-7B) <span class="baseline-badge">B</span></td>
                            <td>53.15</td>
                            <td>53.27</td>
                            <td>52.96</td>
                        </tr>
                        <tr>
                            <td>10</td>
                            <td>UBC-ViL (Baseline-VILA-7B) <span class="baseline-badge">B</span></td>
                            <td>50.49</td>
                            <td>49.44</td>
                            <td>52.19</td>
                        </tr>
                        <tr>
                            <td>11</td>
                            <td>longAI</td>
                            <td>39.27</td>
                            <td>37.44</td>
                            <td>45.14</td>
                        </tr>
                        <tr>
                            <td>12</td>
                            <td>UBC-ViL (Baseline-VideoChat2) <span class="baseline-badge">B</span></td>
                            <td>36.66</td>
                            <td>28.55</td>
                            <td>49.74</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="challenge-links" style="justify-content: flex-start; margin-top: var(--spacing-lg);">
                <a href="{{ '/blackswanchallenge/' | relative_url }}" class="btn btn-secondary">
                    <i class="fas fa-arrow-left"></i> Back to Challenge
                </a>
                <a href="{{ '/blackswansubmissions/' | relative_url }}" class="btn">
                    <i class="fas fa-file-alt"></i> Submission Details
                </a>
            </div>
        </div>
    </div>
</section>
