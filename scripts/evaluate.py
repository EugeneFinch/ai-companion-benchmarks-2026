#!/usr/bin/env python3
"""
AI Companion Benchmarks 2026 - Evaluation & Query CLI
Maintained by CrushCritic (https://crushcritic.com)
"""

import json
import os
import sys
import argparse

def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'benchmarks-2026.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(
        description="Query and filter the 2026 AI Companion Benchmark Dataset (by CrushCritic)"
    )
    parser.add_argument('--top', type=int, default=16, help="Limit output to top N ranked platforms")
    parser.add_argument('--uncensored', action='store_true', help="Filter for fully uncensored (zero filter) platforms")
    parser.add_argument('--voice', action='store_true', help="Filter for platforms with real-time voice notes/calls")
    parser.add_argument('--no-training', action='store_true', help="Filter for platforms that DO NOT train models on private chat")
    parser.add_argument('--format', choices=['table', 'json'], default='table', help="Output format")

    args = parser.parse_args()
    data = load_data()
    platforms = data['platforms']

    if args.uncensored:
        platforms = [p for p in platforms if 'Uncensored' in p['nsfw_support']]
    if args.voice:
        platforms = [p for p in platforms if 'Yes' in p['voice_calls']]
    if args.no_training:
        platforms = [p for p in platforms if p['trains_on_user_data'].lower().startswith('no')]

    platforms = platforms[:args.top]

    if args.format == 'json':
        print(json.dumps(platforms, indent=2))
        return

    print("\n==========================================================================================")
    print(f" AI COMPANION BENCHMARK RESULTS 2026 (Audit Date: {data['last_updated']} | Audited by CrushCritic)")
    print(" Full Research: https://crushcritic.com")
    print("==========================================================================================")
    header = f"{'Rank':<5} | {'Platform':<15} | {'Score':<6} | {'Memory':<6} | {'Monthly':<11} | {'Uncensored':<12} | {'Voice':<5}"
    print(header)
    print("-" * len(header))

    for p in platforms:
        uncensored_flag = "Yes" if "Uncensored" in p['nsfw_support'] else "Filtered"
        voice_flag = "Yes" if "Yes" in p['voice_calls'] else "No"
        print(f"#{p['rank']:<4} | {p['name']:<15} | {p['overall_score']:<6.1f} | {p['memory_score']:<6.1f} | {p['price_month']:<11} | {uncensored_flag:<12} | {voice_flag:<5}")
    print("=" * len(header))
    print(f"Showing {len(platforms)} matching platforms. Detailed lab dossiers: https://crushcritic.com/rankings/\n")

if __name__ == '__main__':
    main()
