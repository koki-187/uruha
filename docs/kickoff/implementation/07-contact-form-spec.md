# 07 Contact Form Specification

## 目的

会社HP、My Agent Series LP、宅建BOOST LPの問い合わせ導線を設計し、商談・資料請求・デモ相談・法人導入相談を受けられる状態にする。

## 基本方針

- 初期は複雑なCRMを組まず、問い合わせを確実に受けることを優先する。
- 会社HPと商品LPでフォーム項目を分ける。
- 自動返信メールと管理者通知を必須にする。
- 将来的にはHubSpot、Notion、Google Sheets、Gmail、LINE通知へ連携する。

---

# 1. フォーム種別

| Form | URL | 目的 | 優先度 |
|---|---|---|---|
| General Contact | `/contact` | 会社全般・協業相談 | High |
| Series Demo Request | `/series#contact` | My Agent Seriesデモ相談 | High |
| TakkenBOOST Contact | `/takken-boost#contact` | 個人申込・法人導入・提携相談 | High |
| Corporate Inquiry | `/takken-boost/business#contact` | 法人ID・団体導入 | Medium |
| Support Inquiry | `/support` | 既存利用者サポート | Later |

---

# 2. 会社HP問い合わせフォーム

## 項目

| Field | Type | Required | Notes |
|---|---|---|---|
| name | text | yes | 氏名 |
| company | text | no | 会社名 |
| email | email | yes | 返信先 |
| phone | tel | no | 初期は任意 |
| inquiry_type | select | yes | 相談種別 |
| message | textarea | yes | 内容 |
| privacy_agree | checkbox | yes | プライバシーポリシー同意 |

## inquiry_type options

- My Agent Seriesについて
- 宅建BOOSTについて
- 協業相談
- DX相談
- 取材・提携
- その他

---

# 3. My Agent Series デモ相談フォーム

## 項目

| Field | Type | Required | Notes |
|---|---|---|---|
| name | text | yes | 氏名 |
| company | text | yes | 会社名または屋号 |
| email | email | yes | 返信先 |
| role | text | no | 役職・担当 |
| business_type | select | yes | 業種 |
| interested_products | checkbox | yes | 関心プロダクト |
| current_issue | textarea | yes | 現在の課題 |
| request_type | select | yes | 希望対応 |
| preferred_contact | select | no | 希望連絡方法 |
| privacy_agree | checkbox | yes | 同意 |

## interested_products options

- MAA Analytics
- MAL Locator
- MAM Much
- MAS Simulate
- MAT Tax AI
- MAR Doc. AI
- まだ分からないので相談したい

## request_type options

- 30分デモを見たい
- 資料がほしい
- 価格を知りたい
- 法人導入を相談したい
- 個別開発を相談したい

---

# 4. 宅建BOOST問い合わせフォーム

## 項目

| Field | Type | Required | Notes |
|---|---|---|---|
| name | text | yes | 氏名 |
| email | email | yes | 返信先 |
| user_type | select | yes | 個人/法人/団体 |
| inquiry_type | select | yes | 問い合わせ種別 |
| organization | text | no | 法人・団体名 |
| code | text | no | 紹介コード・提携コード |
| message | textarea | yes | 内容 |
| privacy_agree | checkbox | yes | 同意 |

## inquiry_type options

- 申込について
- コード適用について
- ログインについて
- PWAインストールについて
- 法人IDについて
- 職能研連携について
- その他

---

# 5. 自動返信メール

## 件名

```txt
【My Agent Works】お問い合わせありがとうございます
```

## 本文案

```txt
お問い合わせありがとうございます。
My Agent Works運営事務局です。

以下の内容でお問い合わせを受け付けました。
内容を確認のうえ、必要に応じて担当よりご連絡いたします。

通常、2〜3営業日以内の返信を目安としております。

※本メールは自動返信です。
```

---

# 6. 管理者通知メール

## 件名

```txt
【HP問い合わせ】{{inquiry_type}} / {{name}}
```

## 通知先

- `info@my-agent.work` 想定
- 初期はGmail転送でも可
- 将来的にGoogle Sheets / Notion / Slack / LINEへ連携

---

# 7. 推奨実装

## 初期

- Formspree
- Google Forms埋め込み
- Resend + API Route
- Cloudflare Pages Functions

## 中期

- HubSpot CRM
- Notion Database
- Google Sheets + Apps Script
- Gmail自動ラベル

## セキュリティ

- reCAPTCHAまたはTurnstile
- rate limit
- honeypot field
- 入力バリデーション
- 個人情報の過剰取得を避ける

---

# 8. CTA配置

| Page | CTA |
|---|---|
| `/` | 導入について相談する |
| `/series` | 30分デモを相談する |
| `/takken-boost` | 申し込み・問い合わせ |
| `/takken-boost/business` | 法人導入を相談する |
| `/trust` | 運用体制について相談する |

## 次アクション

1. `info@my-agent.work` の利用可否を確認する。
2. 初期フォーム方式を決める。
3. 自動返信メールの送信元を決める。
4. プライバシーポリシー同意文を確定する。
5. フォーム送信テストを行う。
