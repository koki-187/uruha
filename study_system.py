#!/usr/bin/env python3
"""
Study System - 勉強管理システム
学習内容を記憶し、ミニテストや本テスト対策を提供するシステム
"""

import json
import os
import random
from datetime import datetime
from typing import List, Dict, Optional


class StudyContent:
    """学習内容を管理するクラス"""
    
    def __init__(self, subject: str, topic: str, content: str, difficulty: int = 1):
        self.subject = subject  # 科目
        self.topic = topic  # トピック
        self.content = content  # 内容
        self.difficulty = difficulty  # 難易度 (1-5)
        self.studied_date = datetime.now().isoformat()
        self.review_count = 0
        self.correct_count = 0
        self.total_attempts = 0
    
    def to_dict(self) -> Dict:
        return {
            'subject': self.subject,
            'topic': self.topic,
            'content': self.content,
            'difficulty': self.difficulty,
            'studied_date': self.studied_date,
            'review_count': self.review_count,
            'correct_count': self.correct_count,
            'total_attempts': self.total_attempts
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        try:
            obj = cls(data['subject'], data['topic'], data['content'], data.get('difficulty', 1))
            obj.studied_date = data.get('studied_date', datetime.now().isoformat())
            obj.review_count = data.get('review_count', 0)
            obj.correct_count = data.get('correct_count', 0)
            obj.total_attempts = data.get('total_attempts', 0)
            return obj
        except KeyError as e:
            raise ValueError(f"学習内容データに必須キーがありません: {e}")
        except Exception as e:
            raise ValueError(f"学習内容データの読み込みに失敗しました: {e}")
    
    def get_accuracy(self) -> float:
        """正答率を計算"""
        if self.total_attempts == 0:
            return 0.0
        return (self.correct_count / self.total_attempts) * 100


class Question:
    """問題を管理するクラス"""
    
    def __init__(self, subject: str, question: str, answer: str, 
                 options: Optional[List[str]] = None, difficulty: int = 1):
        self.subject = subject
        self.question = question
        self.answer = answer
        self.options = options or []
        self.difficulty = difficulty
    
    def to_dict(self) -> Dict:
        return {
            'subject': self.subject,
            'question': self.question,
            'answer': self.answer,
            'options': self.options,
            'difficulty': self.difficulty
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        try:
            return cls(
                data['subject'],
                data['question'],
                data['answer'],
                data.get('options', []),
                data.get('difficulty', 1)
            )
        except KeyError as e:
            raise ValueError(f"問題データに必須キーがありません: {e}")
        except Exception as e:
            raise ValueError(f"問題データの読み込みに失敗しました: {e}")


class StudySystem:
    """学習システムのメインクラス"""
    
    def __init__(self, data_file: str = 'study_data.json'):
        self.data_file = data_file
        self.contents: List[StudyContent] = []
        self.questions: List[Question] = []
        self.load_data()
    
    def load_data(self):
        """データを読み込む"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.contents = [StudyContent.from_dict(c) for c in data.get('contents', [])]
                    self.questions = [Question.from_dict(q) for q in data.get('questions', [])]
            except json.JSONDecodeError as e:
                print(f"⚠️ データファイルの形式が不正です: {e}")
                print(f"   {self.data_file} を確認してください")
                self.contents = []
                self.questions = []
            except ValueError as e:
                print(f"⚠️ データの読み込みエラー: {e}")
                self.contents = []
                self.questions = []
            except Exception as e:
                print(f"⚠️ 予期しないエラー: {e}")
                self.contents = []
                self.questions = []
    
    def save_data(self):
        """データを保存する"""
        data = {
            'contents': [c.to_dict() for c in self.contents],
            'questions': [q.to_dict() for q in self.questions]
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def add_content(self, subject: str, topic: str, content: str, difficulty: int = 1):
        """学習内容を追加"""
        study_content = StudyContent(subject, topic, content, difficulty)
        self.contents.append(study_content)
        self.save_data()
        print(f"✓ 学習内容を追加しました: {subject} - {topic}")
    
    def add_question(self, subject: str, question: str, answer: str, 
                     options: Optional[List[str]] = None, difficulty: int = 1):
        """問題を追加"""
        q = Question(subject, question, answer, options, difficulty)
        self.questions.append(q)
        self.save_data()
        print(f"✓ 問題を追加しました: {subject}")
    
    def get_subjects(self) -> List[str]:
        """すべての科目を取得"""
        subjects = {c.subject for c in self.contents} | {q.subject for q in self.questions}
        return sorted(list(subjects))
    
    def preview_content(self, subject: Optional[str] = None):
        """予習モード - 学習内容を表示"""
        print("\n" + "=" * 50)
        print("📚 予習モード (Preview)")
        print("=" * 50)
        
        contents = self.contents
        if subject:
            contents = [c for c in contents if c.subject == subject]
        
        if not contents:
            print("学習内容がありません。")
            return
        
        for i, content in enumerate(contents, 1):
            print(f"\n【{i}】科目: {content.subject}")
            print(f"   トピック: {content.topic}")
            print(f"   内容: {content.content}")
            print(f"   難易度: {'★' * content.difficulty}")
    
    def review_content(self, subject: Optional[str] = None):
        """復習モード - 学習履歴を確認"""
        print("\n" + "=" * 50)
        print("📝 復習モード (Review)")
        print("=" * 50)
        
        contents = self.contents
        if subject:
            contents = [c for c in contents if c.subject == subject]
        
        if not contents:
            print("復習する内容がありません。")
            return
        
        for i, content in enumerate(contents, 1):
            accuracy = content.get_accuracy()
            print(f"\n【{i}】科目: {content.subject} - {content.topic}")
            print(f"   学習日: {content.studied_date[:10]}")
            print(f"   復習回数: {content.review_count}回")
            print(f"   正答率: {accuracy:.1f}% ({content.correct_count}/{content.total_attempts})")
            content.review_count += 1
        
        self.save_data()
    
    def generate_mini_test(self, subject: Optional[str] = None, num_questions: int = 5):
        """ミニテストを生成"""
        print("\n" + "=" * 50)
        print("✏️  ミニテスト (Mini Test)")
        print("=" * 50)
        
        questions = self.questions
        if subject:
            questions = [q for q in questions if q.subject == subject]
        
        if not questions:
            print("問題がありません。")
            return
        
        selected = random.sample(questions, min(num_questions, len(questions)))
        score = 0
        
        for i, q in enumerate(selected, 1):
            print(f"\n問題 {i}: {q.question}")
            if q.options:
                for j, opt in enumerate(q.options, 1):
                    print(f"  {j}. {opt}")
            
            user_answer = input("答え: ").strip()
            
            if user_answer.lower() == q.answer.lower():
                print("✓ 正解！")
                score += 1
                self._update_content_stats(q.subject, True)
            else:
                print(f"✗ 不正解。正解は: {q.answer}")
                self._update_content_stats(q.subject, False)
        
        print(f"\n結果: {score}/{len(selected)} 問正解 ({(score/len(selected)*100):.1f}%)")
        self.save_data()
    
    def generate_full_test(self, subject: Optional[str] = None):
        """本テストを生成"""
        print("\n" + "=" * 50)
        print("📋 本テスト (Full Test)")
        print("=" * 50)
        
        questions = self.questions
        if subject:
            questions = [q for q in questions if q.subject == subject]
        
        if not questions:
            print("問題がありません。")
            return
        
        score = 0
        
        for i, q in enumerate(questions, 1):
            print(f"\n問題 {i}: {q.question}")
            print(f"難易度: {'★' * q.difficulty}")
            if q.options:
                for j, opt in enumerate(q.options, 1):
                    print(f"  {j}. {opt}")
            
            user_answer = input("答え: ").strip()
            
            if user_answer.lower() == q.answer.lower():
                print("✓ 正解！")
                score += 1
                self._update_content_stats(q.subject, True)
            else:
                print(f"✗ 不正解。正解は: {q.answer}")
                self._update_content_stats(q.subject, False)
        
        print(f"\n最終結果: {score}/{len(questions)} 問正解 ({(score/len(questions)*100):.1f}%)")
        self.save_data()
    
    def show_weak_subjects(self):
        """苦手科目を表示"""
        print("\n" + "=" * 50)
        print("📉 苦手科目分析 (Weak Subjects)")
        print("=" * 50)
        
        subject_stats = {}
        
        for content in self.contents:
            if content.subject not in subject_stats:
                subject_stats[content.subject] = {
                    'correct': 0,
                    'total': 0
                }
            subject_stats[content.subject]['correct'] += content.correct_count
            subject_stats[content.subject]['total'] += content.total_attempts
        
        if not subject_stats:
            print("まだ統計データがありません。")
            return
        
        weak_subjects = []
        for subject, stats in subject_stats.items():
            if stats['total'] > 0:
                accuracy = (stats['correct'] / stats['total']) * 100
                weak_subjects.append((subject, accuracy, stats['correct'], stats['total']))
        
        weak_subjects.sort(key=lambda x: x[1])
        
        if not weak_subjects:
            print("まだテストを受けていません。")
            return
        
        print("\n苦手な順:")
        for i, (subject, accuracy, correct, total) in enumerate(weak_subjects, 1):
            status = "⚠️" if accuracy < 60 else "📊"
            print(f"{i}. {status} {subject}: {accuracy:.1f}% ({correct}/{total})")
        
        if weak_subjects and weak_subjects[0][1] < 60:
            weakest = weak_subjects[0][0]
            print(f"\n💡 おすすめ: 「{weakest}」を重点的に復習しましょう！")
    
    def _update_content_stats(self, subject: str, is_correct: bool):
        """学習内容の統計を更新"""
        for content in self.contents:
            if content.subject == subject:
                content.total_attempts += 1
                if is_correct:
                    content.correct_count += 1


def main():
    """メイン関数"""
    system = StudySystem()
    
    print("=" * 50)
    print("  学習管理システム (Study System)")
    print("=" * 50)
    
    while True:
        print("\n【メニュー】")
        print("1. 学習内容を追加")
        print("2. 問題を追加")
        print("3. 予習 (Preview)")
        print("4. 復習 (Review)")
        print("5. ミニテスト")
        print("6. 本テスト")
        print("7. 苦手科目分析")
        print("8. 科目一覧")
        print("0. 終了")
        
        choice = input("\n選択してください: ").strip()
        
        if choice == '1':
            subject = input("科目: ").strip()
            topic = input("トピック: ").strip()
            content = input("内容: ").strip()
            difficulty = input("難易度 (1-5): ").strip()
            try:
                difficulty = int(difficulty) if difficulty else 1
                difficulty = max(1, min(5, difficulty))  # 1-5の範囲に制限
            except ValueError:
                difficulty = 1
            system.add_content(subject, topic, content, difficulty)
        
        elif choice == '2':
            subject = input("科目: ").strip()
            question = input("問題: ").strip()
            answer = input("答え: ").strip()
            has_options = input("選択肢を追加しますか？ (y/n): ").strip().lower()
            options = []
            if has_options == 'y':
                try:
                    num_options = int(input("選択肢の数: ").strip())
                    for i in range(num_options):
                        opt = input(f"選択肢 {i+1}: ").strip()
                        options.append(opt)
                except ValueError:
                    print("⚠️ 数値を入力してください。選択肢なしで登録します。")
            difficulty = input("難易度 (1-5): ").strip()
            try:
                difficulty = int(difficulty) if difficulty else 1
                difficulty = max(1, min(5, difficulty))  # 1-5の範囲に制限
            except ValueError:
                difficulty = 1
            system.add_question(subject, question, answer, options, difficulty)
        
        elif choice == '3':
            subjects = system.get_subjects()
            if subjects:
                print("\n科目:", ", ".join(subjects))
                subject = input("科目を選択 (空白で全て): ").strip()
                system.preview_content(subject if subject else None)
            else:
                system.preview_content()
        
        elif choice == '4':
            subjects = system.get_subjects()
            if subjects:
                print("\n科目:", ", ".join(subjects))
                subject = input("科目を選択 (空白で全て): ").strip()
                system.review_content(subject if subject else None)
            else:
                system.review_content()
        
        elif choice == '5':
            subjects = system.get_subjects()
            if subjects:
                print("\n科目:", ", ".join(subjects))
                subject = input("科目を選択 (空白で全て): ").strip()
                num = input("問題数 (デフォルト: 5): ").strip()
                try:
                    num = int(num) if num else 5
                    num = max(1, num)  # 最低1問
                except ValueError:
                    num = 5
                system.generate_mini_test(subject if subject else None, num)
            else:
                system.generate_mini_test()
        
        elif choice == '6':
            subjects = system.get_subjects()
            if subjects:
                print("\n科目:", ", ".join(subjects))
                subject = input("科目を選択 (空白で全て): ").strip()
                system.generate_full_test(subject if subject else None)
            else:
                system.generate_full_test()
        
        elif choice == '7':
            system.show_weak_subjects()
        
        elif choice == '8':
            subjects = system.get_subjects()
            if subjects:
                print("\n登録されている科目:")
                for i, subj in enumerate(subjects, 1):
                    print(f"  {i}. {subj}")
            else:
                print("\nまだ科目が登録されていません。")
        
        elif choice == '0':
            print("\n学習システムを終了します。")
            break
        
        else:
            print("無効な選択です。")


if __name__ == "__main__":
    main()
