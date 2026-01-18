#!/usr/bin/env python3
"""
使用例 - 学習の流れを示すスクリプト
"""

import os
import shutil
from study_system import StudySystem


def usage_example():
    """学習の一連の流れを示す"""
    print("=" * 70)
    print("  学習管理システム - 使用例")
    print("  推奨される学習フローを実演します")
    print("=" * 70)
    print()
    
    # セットアップ
    if os.path.exists("example_study_data.json"):
        shutil.copy("example_study_data.json", "usage_demo.json")
        system = StudySystem("usage_demo.json")
    else:
        print("✗ example_study_data.json が見つかりません")
        return
    
    # フェーズ1: 予習（学習前）
    print("\n" + "=" * 70)
    print("【フェーズ1】予習 - テスト範囲の確認")
    print("=" * 70)
    print("\n科目「数学」の学習内容を確認します...")
    print()
    
    math_contents = [c for c in system.contents if c.subject == "数学"]
    for i, content in enumerate(math_contents, 1):
        print(f"{i}. {content.topic}")
        print(f"   内容: {content.content}")
        print(f"   難易度: {'★' * content.difficulty}")
        print()
    
    print("💡 学習のポイント:")
    print("   - 各トピックの基本概念を理解する")
    print("   - 難易度が高いものは時間をかけて学習する")
    print("   - 不明点は調べてから次に進む")
    
    # フェーズ2: ミニテストで理解度チェック
    print("\n" + "=" * 70)
    print("【フェーズ2】ミニテスト - 理解度の確認")
    print("=" * 70)
    print("\n学習後、短いテストで理解度を確認します")
    print()
    
    math_questions = [q for q in system.questions if q.subject == "数学"]
    print(f"数学の問題数: {len(math_questions)}問")
    print("推奨: まず5問程度のミニテストを受ける")
    print()
    
    # テスト結果をシミュレート
    print("--- ミニテストの例 ---")
    for i, q in enumerate(math_questions[:2], 1):
        print(f"\n問題{i}: {q.question}")
        if q.options:
            for j, opt in enumerate(q.options, 1):
                print(f"  {j}. {opt}")
        print(f"正解: {q.answer}")
    
    # フェーズ3: 復習
    print("\n" + "=" * 70)
    print("【フェーズ3】復習 - 間違えた問題の確認")
    print("=" * 70)
    print("\nテスト結果に基づいて復習します")
    print()
    
    # 統計を追加
    for content in system.contents:
        if content.subject == "数学":
            content.total_attempts = 5
            content.correct_count = 4  # 80%の正答率
        elif content.subject == "英語":
            content.total_attempts = 5
            content.correct_count = 3  # 60%の正答率
        elif content.subject == "歴史":
            content.total_attempts = 5
            content.correct_count = 2  # 40%の正答率
    
    system.save_data()
    
    print("テスト結果:")
    print("  数学: 80% (4/5) - よくできています！")
    print("  英語: 60% (3/5) - もう少し復習が必要")
    print("  歴史: 40% (2/5) - 重点的に復習しましょう")
    
    # フェーズ4: 苦手科目の特定と対策
    print("\n" + "=" * 70)
    print("【フェーズ4】苦手科目の特定と克服")
    print("=" * 70)
    print()
    
    # 苦手科目を分析
    subject_stats = {}
    for content in system.contents:
        if content.subject not in subject_stats:
            subject_stats[content.subject] = {
                'correct': 0,
                'total': 0
            }
        subject_stats[content.subject]['correct'] += content.correct_count
        subject_stats[content.subject]['total'] += content.total_attempts
    
    weak_subjects = []
    for subject, stats in subject_stats.items():
        if stats['total'] > 0:
            accuracy = (stats['correct'] / stats['total']) * 100
            weak_subjects.append((subject, accuracy))
    
    weak_subjects.sort(key=lambda x: x[1])
    
    print("科目別の正答率:")
    for subject, accuracy in weak_subjects:
        status = "⚠️ 要復習" if accuracy < 60 else "✓ 良好"
        print(f"  {subject}: {accuracy:.1f}% - {status}")
    
    if weak_subjects[0][1] < 60:
        print(f"\n💡 対策: 「{weak_subjects[0][0]}」を優先的に復習しましょう")
        print(f"   1. {weak_subjects[0][0]}の学習内容を再確認")
        print(f"   2. {weak_subjects[0][0]}の問題を繰り返し解く")
        print(f"   3. 理解できない部分は調べる・質問する")
    
    # フェーズ5: 本テスト
    print("\n" + "=" * 70)
    print("【フェーズ5】本テスト - 総合力の測定")
    print("=" * 70)
    print("\n復習後、本テストで最終確認します")
    print()
    
    print("本テストの特徴:")
    print("  - 全科目の全問題を出題")
    print("  - 難易度も表示される")
    print("  - 総合的な理解度を測定")
    print()
    
    total_questions = len(system.questions)
    print(f"問題総数: {total_questions}問")
    print("目標正答率: 80%以上")
    
    # 学習サイクル
    print("\n" + "=" * 70)
    print("【継続的な学習サイクル】")
    print("=" * 70)
    print()
    print("1. 予習 📚 → 新しい内容を学ぶ")
    print("2. ミニテスト ✏️ → すぐに理解度を確認")
    print("3. 復習 📝 → 間違いを見直す")
    print("4. 苦手科目克服 📉 → 弱点を強化")
    print("5. 本テスト 📋 → 総合力を確認")
    print()
    print("このサイクルを繰り返すことで、確実に学力が向上します！")
    
    # まとめ
    print("\n" + "=" * 70)
    print("【まとめ】")
    print("=" * 70)
    print()
    print("✓ 予習で基礎を固める")
    print("✓ ミニテストで小まめに確認")
    print("✓ 復習で知識を定着")
    print("✓ 苦手科目を重点的に学習")
    print("✓ 本テストで実力を測定")
    print()
    print("このシステムを使って、効率的に学習を進めましょう！")
    
    # クリーンアップ
    if os.path.exists("usage_demo.json"):
        os.remove("usage_demo.json")


if __name__ == "__main__":
    usage_example()
