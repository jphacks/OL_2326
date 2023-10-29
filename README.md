# ProdTalk Master
<img width="931" alt="image" src="https://github.com/jphacks/OL_2326/assets/131417565/7e7f11c5-e0a6-41ee-b1f4-38d0082956f6">

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2023/07/JPHACKS2023_ogp.png)](https://www.youtube.com/watch?v=yYRQEdfGjEg)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
アフターコロナ　日本の経済低迷　グローバル化・・・
### 製品説明（具体的な製品の説明）
ProdTalk Masterは日本の中堅中小企業向けに提供される英語教育サービスです。
海外ブースの出展や海外展開に備え、全社員が自社のサービスを英語でプレゼンテーションできる実践的な英語力を養うことを目的としています。
日々行われる英語プレゼン練習を、AIが採点し、改善点を提案。これにより、社員は実践的かつ効果的に英語表現スキルを向上させ、国際的な舞台での自信を築くことができます。
また、システム全体でデータを収集・解析することで、社員教育の担当者は英語教育の効果を容易に測定できます。

### 特長
#### 1. 特長1
*　非英語話者向けにチューニングされたAIによる発話の採点、生成AIを用いた発話文の改善点提案
#### 2. 特長2
*　生成AIを用いた発話文の改善提案
#### 3. 特長3
*　スコアなどの統計情報を可視化し、社内教育のDX化に貢献

### 解決出来ること
* アフターコロナのグローバル化の再開や、日本の経済縮小という社会課題に対応
* 通訳や他の翻訳サービスに比べ、迅速かつ安価
* 仕事で活きる実践的な英語教育


### 今後の展望
* 発話文の改善点提案の精度改善に向けた、言語モデルのファインチューニングとプロプロンプトエンジニアリング
  現段階のプロプロンプトはChatGPTに生成AIにわかりやすいプロンプトを生成するよう依頼したものを改良したものを使用
* 音声だけでなく動画による動作データを含めた、統計データの充実化、可視化手法の洗練化
* 

### 注力したこと（こだわり等）
* 約２時間分の非ネイティブ話者の音声データを学習したSVMによる自動採点
* 文字起こしや文章生成には、事前学習済みモデルを活用
* 実際のユースケースを意識した使いやすいUI

## 開発技術
### 活用した技術
#### API・データ
* Avalinguo-Audio-Set(Dataset for Speaker Fluency Level Classification)
  https://github.com/agrija9/Avalinguo-Audio-Set#avalinguo-audio-dataset-dataset-for-speaker-fluency-level-classification


#### フレームワーク・ライブラリ・モジュール
* django
* Whisper（OpenAI）　https://github.com/openai/whisper
* FLAN T5（Google）　https://huggingface.co/docs/transformers/model_doc/flan-t5

#### デバイス
* スマートフォン（従業員の録音録画）
* ブラウザ（結果表示や、管理者画面）

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 非ネイティブ話者の音声データを学習したSVMによる自動採点
  https://github.com/jphacks/OL_2326/blob/develop/TYouF/training/lib/inference.py
  元の学習データが5秒ずつに区切られたものであるため、採点時も録音された音声を5秒ごとに区切り推論を行う。
