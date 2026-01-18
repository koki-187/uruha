#!/usr/bin/env python3
"""
テストスクリプト - 学習システムの機能をテスト
"""

import os
import sys
import json
from study_system import StudySystem, StudyContent, Question


def test_basic_operations():
    """基本操作のテスト"""
    print("=" * 60)
    print("テスト1: 基本操作")
    print("=" * 60)
    
    # テストデータファイル
    test_file = "test_study_data.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    # システムを初期化
    system = StudySystem(test_file)
    
    # 学習内容を追加
    system.add_content("数学", "二次方程式", "ax² + bx + c = 0", 3)
    system.add_content("英語", "現在完了", "have/has + 過去分詞", 2)
    
    # 問題を追加
    system.add_question("数学", "1 + 1 = ?", "2", ["1", "2", "3", "4"], 1)
    system.add_question("英語", "I ( ) lived here for 5 years.", "have", ["has", "have", "had"], 2)
    
    # データが保存されているか確認
    assert os.path.exists(test_file), "データファイルが作成されていません"
    
    # 科目一覧を確認
    subjects = system.get_subjects()
    assert "数学" in subjects, "数学が登録されていません"
    assert "英語" in subjects, "英語が登録されていません"
    
    print("✓ 学習内容と問題の追加: 成功")
    print("✓ データの保存: 成功")
    print("✓ 科目一覧の取得: 成功")
    
    # クリーンアップ
    if os.path.exists(test_file):
        os.remove(test_file)
    
    return True


def test_data_persistence():
    """データの永続化テスト"""
    print("\n" + "=" * 60)
    print("テスト2: データの永続化")
    print("=" * 60)
    
    test_file = "test_persistence.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    # データを追加
    system1 = StudySystem(test_file)
    system1.add_content("理科", "光合成", "6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂", 2)
    system1.add_question("理科", "光合成に必要なものは?", "光、水、二酸化炭素", [], 2)
    
    # 新しいインスタンスで読み込み
    system2 = StudySystem(test_file)
    
    # データが保持されているか確認
    assert len(system2.contents) == 1, "学習内容が読み込まれていません"
    assert len(system2.questions) == 1, "問題が読み込まれていません"
    assert system2.contents[0].subject == "理科", "科目が正しく読み込まれていません"
    
    print("✓ データの永続化: 成功")
    
    # クリーンアップ
    if os.path.exists(test_file):
        os.remove(test_file)
    
    return True


def test_statistics():
    """統計機能のテスト"""
    print("\n" + "=" * 60)
    print("テスト3: 統計機能")
    print("=" * 60)
    
    test_file = "test_stats.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    system = StudySystem(test_file)
    system.add_content("数学", "算数", "基礎計算", 1)
    
    # 統計を更新
    content = system.contents[0]
    content.total_attempts = 10
    content.correct_count = 7
    
    # 正答率を計算
    accuracy = content.get_accuracy()
    assert accuracy == 70.0, f"正答率の計算が正しくありません: {accuracy}"
    
    print(f"✓ 正答率計算: 成功 (70.0%)")
    
    # クリーンアップ
    if os.path.exists(test_file):
        os.remove(test_file)
    
    return True


def test_example_data():
    """サンプルデータのテスト"""
    print("\n" + "=" * 60)
    print("テスト4: サンプルデータ")
    print("=" * 60)
    
    example_file = "example_study_data.json"
    
    # サンプルデータが存在するか確認
    assert os.path.exists(example_file), "サンプルデータファイルが存在しません"
    
    # サンプルデータを読み込み
    with open(example_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # データの構造を確認
    assert 'contents' in data, "contentsキーがありません"
    assert 'questions' in data, "questionsキーがありません"
    assert len(data['contents']) > 0, "学習内容が空です"
    assert len(data['questions']) > 0, "問題が空です"
    
    # システムでサンプルデータを読み込み
    test_file = "test_example.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    # サンプルデータをコピー
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    system = StudySystem(test_file)
    
    # データが正しく読み込まれたか確認
    assert len(system.contents) > 0, "学習内容が読み込まれていません"
    assert len(system.questions) > 0, "問題が読み込まれていません"
    
    subjects = system.get_subjects()
    print(f"✓ 読み込まれた科目: {', '.join(subjects)}")
    print(f"✓ 学習内容数: {len(system.contents)}")
    print(f"✓ 問題数: {len(system.questions)}")
    
    # クリーンアップ
    if os.path.exists(test_file):
        os.remove(test_file)
    
    return True


def run_all_tests():
    """すべてのテストを実行"""
    print("\n" + "=" * 60)
    print("学習システムのテストを開始します")
    print("=" * 60 + "\n")
    
    tests = [
        test_basic_operations,
        test_data_persistence,
        test_statistics,
        test_example_data
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"✗ テスト失敗: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"テスト結果: {passed}個成功, {failed}個失敗")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
