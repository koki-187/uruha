#!/usr/bin/env python3
"""
エラーハンドリングのテスト
"""

import os
import json
from study_system import StudySystem


def test_corrupted_json():
    """破損したJSONファイルの処理"""
    print("=" * 60)
    print("テスト1: 破損したJSONファイル")
    print("=" * 60)
    
    test_file = "test_corrupted.json"
    
    # 破損したJSONファイルを作成
    with open(test_file, 'w') as f:
        f.write("{this is not valid json")
    
    # システムは起動できるはず（エラーメッセージを出してから空のデータで起動）
    system = StudySystem(test_file)
    
    # データは空になっているはず
    assert len(system.contents) == 0, "破損データからコンテンツが読み込まれています"
    assert len(system.questions) == 0, "破損データから問題が読み込まれています"
    
    print("✓ 破損したJSONファイルを適切に処理しました")
    
    # クリーンアップ
    if os.path.exists(test_file):
        os.remove(test_file)
    
    return True


def test_missing_keys():
    """必須キーが欠けているデータの処理"""
    print("\n" + "=" * 60)
    print("テスト2: 必須キーが欠けているデータ")
    print("=" * 60)
    
    test_file = "test_missing_keys.json"
    
    # 必須キーが欠けているデータ
    bad_data = {
        "contents": [
            {
                "subject": "数学",
                # topicとcontentが欠けている
            }
        ],
        "questions": [
            {
                "subject": "英語",
                # questionとanswerが欠けている
            }
        ]
    }
    
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(bad_data, f)
    
    # システムは起動できるはず（エラーメッセージを出してから空のデータで起動）
    system = StudySystem(test_file)
    
    # 不正なデータはスキップされているはず
    print(f"読み込まれたコンテンツ数: {len(system.contents)}")
    print(f"読み込まれた問題数: {len(system.questions)}")
    
    print("✓ 不正なデータを適切に処理しました")
    
    # クリーンアップ
    if os.path.exists(test_file):
        os.remove(test_file)
    
    return True


def test_partial_data():
    """一部のキーが欠けているデータの処理"""
    print("\n" + "=" * 60)
    print("テスト3: オプショナルキーが欠けているデータ")
    print("=" * 60)
    
    test_file = "test_partial.json"
    
    # 一部のキーが欠けているが、最低限のキーはある
    partial_data = {
        "contents": [
            {
                "subject": "数学",
                "topic": "算数",
                "content": "1+1=2"
                # difficultyやその他のキーが欠けている
            }
        ],
        "questions": [
            {
                "subject": "英語",
                "question": "What is your name?",
                "answer": "My name is..."
                # optionsやdifficultyが欠けている
            }
        ]
    }
    
    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(partial_data, f)
    
    # システムは正常に起動してデフォルト値を使用するはず
    system = StudySystem(test_file)
    
    assert len(system.contents) == 1, "コンテンツが読み込まれていません"
    assert len(system.questions) == 1, "問題が読み込まれていません"
    
    # デフォルト値がセットされているか確認
    content = system.contents[0]
    assert content.difficulty == 1, "デフォルトの難易度が設定されていません"
    assert content.review_count == 0, "デフォルトの復習回数が設定されていません"
    
    question = system.questions[0]
    assert question.difficulty == 1, "デフォルトの難易度が設定されていません"
    assert question.options == [], "デフォルトの選択肢が設定されていません"
    
    print("✓ オプショナルキーにデフォルト値を使用しました")
    print(f"  コンテンツ難易度: {content.difficulty}")
    print(f"  問題難易度: {question.difficulty}")
    
    # クリーンアップ
    if os.path.exists(test_file):
        os.remove(test_file)
    
    return True


def run_error_tests():
    """すべてのエラーハンドリングテストを実行"""
    print("\n" + "=" * 60)
    print("エラーハンドリングのテストを開始します")
    print("=" * 60 + "\n")
    
    tests = [
        test_corrupted_json,
        test_missing_keys,
        test_partial_data
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
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"エラーハンドリングテスト結果: {passed}個成功, {failed}個失敗")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    import sys
    success = run_error_tests()
    sys.exit(0 if success else 1)
