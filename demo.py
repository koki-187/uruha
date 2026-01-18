#!/usr/bin/env python3
"""
デモスクリプト - 学習システムの機能をデモンストレーション
"""

import os
import shutil
from study_system import StudySystem


def demo():
    """システムのデモを実行"""
    print("=" * 60)
    print("  学習管理システム - デモンストレーション")
    print("=" * 60)
    print()
    
    # サンプルデータをコピー
    if os.path.exists("example_study_data.json"):
        shutil.copy("example_study_data.json", "demo_data.json")
        system = StudySystem("demo_data.json")
        print("✓ サンプルデータを読み込みました")
    else:
        print("✗ example_study_data.json が見つかりません")
        return
    
    # 1. 科目一覧を表示
    print("\n" + "=" * 60)
    print("1. 登録されている科目")
    print("=" * 60)
    subjects = system.get_subjects()
    for i, subject in enumerate(subjects, 1):
        print(f"  {i}. {subject}")
    
    # 2. 予習モード
    print("\n" + "=" * 60)
    print("2. 予習モード - 数学の学習内容")
    print("=" * 60)
    system.preview_content("数学")
    
    # 3. 復習モード
    print("\n" + "=" * 60)
    print("3. 復習モード - 全科目の学習状況")
    print("=" * 60)
    system.review_content()
    
    # 4. 苦手科目分析（初期状態）
    print("\n" + "=" * 60)
    print("4. 苦手科目分析（テスト前）")
    print("=" * 60)
    system.show_weak_subjects()
    
    # 5. 統計情報を追加（テストをシミュレート）
    print("\n" + "=" * 60)
    print("5. テスト結果をシミュレート")
    print("=" * 60)
    
    # 数学: 高得点
    for content in system.contents:
        if content.subject == "数学":
            content.total_attempts = 10
            content.correct_count = 9
    
    # 英語: 中得点
    for content in system.contents:
        if content.subject == "英語":
            content.total_attempts = 10
            content.correct_count = 6
    
    # 歴史: 低得点
    for content in system.contents:
        if content.subject == "歴史":
            content.total_attempts = 10
            content.correct_count = 4
    
    system.save_data()
    print("✓ テスト結果を記録しました")
    print("  - 数学: 90% (9/10)")
    print("  - 英語: 60% (6/10)")
    print("  - 歴史: 40% (4/10)")
    
    # 6. 苦手科目分析（テスト後）
    print("\n" + "=" * 60)
    print("6. 苦手科目分析（テスト後）")
    print("=" * 60)
    system.show_weak_subjects()
    
    # 7. 問題の例
    print("\n" + "=" * 60)
    print("7. 登録されている問題の例")
    print("=" * 60)
    for i, question in enumerate(system.questions[:3], 1):
        print(f"\n問題 {i} ({question.subject}):")
        print(f"  Q: {question.question}")
        if question.options:
            print(f"  選択肢: {', '.join(question.options)}")
        print(f"  A: {question.answer}")
        print(f"  難易度: {'★' * question.difficulty}")
    
    print("\n" + "=" * 60)
    print("デモンストレーション完了")
    print("=" * 60)
    print("\n実際にシステムを使うには:")
    print("  python3 study_system.py")
    print("\nサンプルデータを使う場合:")
    print("  cp example_study_data.json study_data.json")
    print("  python3 study_system.py")
    
    # クリーンアップ
    if os.path.exists("demo_data.json"):
        os.remove("demo_data.json")


if __name__ == "__main__":
    demo()
