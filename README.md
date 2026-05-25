# 🤖 RAG Chatbot — LangChain + Groq + Streamlit

A production-ready Retrieval-Augmented Generation (RAG) chatbot built with
**LangChain**, **Groq** (free & fast LLM inference), and **Streamlit**.
Upload your own documents, ask questions, and get grounded answers — all
running locally or on Streamlit Cloud.

---

## ✨ Features

- **Hybrid retrieval** — BM25 keyword search + Chroma vector search fused with
  Reciprocal Rank Fusion (RRF) for best-of-both results
- **Free embeddings** — `sentence-transformers/all-MiniLM-L6-v2` runs locally,
  no embedding API key needed
- **Groq LLM** — ultra-fast inference via `llama3-70b-8192` (free tier
  available)
- **Conversation memory** — chat history is preserved across turns in the
  Streamlit session
- **Zero OpenAI dependency** — completely removed

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM | Groq (`llama3-70b-8192`) |
| Orchestration | LangChain |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` (local) |
| Vector store | Chroma |
| Keyword retrieval | BM25 (`rank-bm25`) |
| Hybrid fusion | LangChain `EnsembleRetriever` |

---

## 🚀 Quick Start

### 1 — Clone the repo

```bash
git clone https://github.com/<your-username>/example-app-langchain-rag.git
cd example-app-langchain-rag
```

### 2 — Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3 — Install dependencies

```bash
pip install -U pip
pip install -r requirements.txt
```

<<<<<<< HEAD
### 4 — Get a free Groq API key

1. Visit <https://console.groq.com>
2. Sign up / log in
3. Create an API key

### 5 — Set up secrets

```bash
mkdir .streamlit
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # or create manually
```

Edit `.streamlit/secrets.toml`:

```toml
GROQ_API_KEY = "gsk_your_key_here"
```

> **Tip:** You can also paste the key directly into the sidebar at runtime —
> no file needed for local testing.

### 6 — Add your documents

Drop `.txt`, `.pdf`, or `.md` files into the `data/` directory.

### 7 — Run the app
=======
If you run into issues related to hnswlib or chroma-hnswlib while installing requirements you may need to install system package for the underlying package.

For example, on Ubuntu 22.04 this was needed before pip install of hnswlib would succeed.

```bash
sudo apt install python3-hnswlib
```

### Setup .env file with API tokens needed.

```
OPENAI_API_KEY="<Put your token here>"
HUGGINGFACEHUB_API_TOKEN="<Put your token here>"
```

### Setup Streamlit app secrets.

#### 1. Set up the .streamlit directory and secrets file.

```bash
mkdir .streamlit
touch .streamlit/secrets.toml
chmod 0600 .streamlit/secrets.toml
```

#### 2. Edit secrets.toml

**Either edit `secrets.toml` in you favorite editor.**

```toml
OPENAI_API_KEY="<Put your token here>"
HUGGINGFACEHUB_API_TOKEN="<Put your token here>"
```

**Or, you can just reuse .env contents from above.**

```bash
cat < .env >> .streamlit/secrets.toml
```

### Verify Environment

1. Check that LangChain dependencies are working.

```bash
python basic_chain.py
```

2. Check that Streamlit and dependencies are working.
>>>>>>> 83d150474fd50d8dae19df2ecf2b57c061bfa497

```bash
streamlit run streamlit_app.py
```

<<<<<<< HEAD
---

## ☁️ Deploy to Streamlit Cloud

1. Push your fork to GitHub
2. Go to <https://share.streamlit.io> → **New app**
3. Point it at `streamlit_app.py`
4. In **Advanced settings → Secrets**, add:
   ```
   GROQ_API_KEY = "gsk_your_key_here"
   ```
5. Deploy 🎉

---

## 📁 Project Structure

```
├── streamlit_app.py      # Main Streamlit UI
├── basic_chain.py        # LLM initialisation (Groq)
├── full_chain.py         # Full RAG + memory chain
├── ensemble.py           # Hybrid BM25 + vector retriever
├── rag_chain.py          # RAG chain builder
├── memory.py             # Conversation memory wrapper
├── local_loader.py       # Load files from data/
├── remote_loader.py      # Load web pages
├── splitter.py           # Document splitting
├── vector_store.py       # Chroma vector DB helpers
├── data/                 # ← put your documents here
├── examples/             # Sample documents
├── requirements.txt
└── .streamlit/
    └── secrets.toml      # API keys (git-ignored)
```

---

## 🔧 Configuration

| Variable | Where | Description |
|---|---|---|
| `GROQ_API_KEY` | `.streamlit/secrets.toml` or sidebar | Groq API key |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Commit your changes: `git commit -m "feat: add my feature"`
4. Push: `git push origin feat/my-feature`
5. Open a Pull Request

---

## 📄 License

[Apache 2.0](LICENSE)

---

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io) for the original example app
- [LangChain](https://langchain.com) for the RAG framework
- [Groq](https://groq.com) for blazing-fast free LLM inference
=======
3. Run Individual Example Programs

The most of the Python source files besides `streamlit_app.py` have a main defined
so that you can execute them directly as an example or test.

For example, the main in `ensemble.py` will use context from an online version of the book [*The Problems of Philosophy* by Bertrand Russell](https://www.gutenberg.org/ebooks/5827.html.images)
to answer "What are the key problems of philosophy according to Russell?"

```bash
python ensemble.py
```

>    Split into 313 chunks
>    According to Russell, the key problems of philosophy include the uncertainty of knowledge, the limitations of metaphysical reasoning, and the inability to provide definite answers to fundamental questions. Philosophy aims to diminish the risk of error, but cannot eliminate it entirely due to human fallibility. The value of philosophy lies in its ability to challenge common sense beliefs and lead to the exploration of complex problems.



## Example Queries for Streamlit App

### Example 1: Metabolic Rate

**Question:**
If I am an 195 lb male, what should my calorie intake be to lose 1 lb a week based on what you know about my basal metabolic rate?

**Answer:**
To calculate the calorie intake for a 195 lb male to lose 1 lb per week based on their basal metabolic rate, we can use the estimated BMR values provided in the context.

For a 190 lb male, the estimated BMR is around 2,280 calories per day. To lose 1 lb per week, a general rule of thumb is to create a calorie deficit of about 500 calories per day.

Therefore, to lose 1 lb per week, a 195 lb male should aim to consume around 1,780 calories per day (2,280 calories - 500 calories). This calorie intake, combined with regular physical activity, can help achieve a sustainable weight loss goal.

### Example 2: Recipes

NOTE: to use this example, copy the `example/us_army_recipes.txt` file into the `data` directory. It is left out by default because it significantly increases the resources used over the other examples.

**Question:**
How do I make salmon croquettes according to the recipes I provided you?

**Answer:**
To make salmon croquettes based on the recipes shared, you can follow these steps:

Ingredients:

- 4 cans of salmon
- 4 pounds of cold boiled potatoes
- 2 eggs
- Salt and pepper to taste
- Cracker dust for coating
- Oil for frying

Instructions:

1. Drain the canned salmon and remove any bones or skin.
2. In a large bowl, mash the salmon and boiled potatoes together.
3. Add the eggs, salt, and pepper to the mixture and combine well.
4. Shape the mixture into small cakes about 2 inches in diameter.
5. In a separate bowl, beat the remaining eggs with a little milk to create an egg batter.
6. Dip each salmon cake into the egg batter, then coat it with cracker dust.
7. Heat oil in a pan for frying.
8. Fry the salmon croquettes in the hot oil until they are golden brown on all sides.
9. Once cooked, remove them from the oil and place them on a paper towel to drain any excess oil.
10. Serve the salmon croquettes hot and enjoy!

I hope these instructions help you make delicious salmon croquettes! Let me know if you need any more assistance.


## Example Data Used

* The file `examples/nutrients_csvfile.csv` is from the Kaggle Dataset [Nutritional Facts for most common foods](https://www.kaggle.com/datasets/niharika41298/nutrition-details-for-most-common-foods/)
shared under the [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/) license.
* The file `examples/us_army_recipes.txt` is in the public domain, and was retrieved from Project Gutenberg at [Recipes Used in the Cooking Schools, U. S. Army by United States. Army](https://www.gutenberg.org/ebooks/65250).
* The file `examples/healthy_meal_10_tips.pdf` was published by thes USDA, Center for Nutrition Policy and Promotion and was retrieved from Wikimedia  Commons, and is in the public domain.
[See page for author, Public domain, via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Build_a_healthy_meal_10_tips_for_healthy_meals_(IA_CAT31299650).pdf).
* The file `examples/mal_boole.pdf` is in the public domain. Boole, G. (1847, January 1). The Mathematical Analysis of Logic. Retrieved from Project Gutenberg at https://www.gutenberg.org/ebooks/36884.
* The file `examples/grocery.md` is just a grocery list.

## References


Gordon V. Cormack, Charles L A Clarke, and Stefan Buettcher. 2009. [Reciprocal rank fusion outperforms condorcet and individual rank learning methods](https://dl.acm.org/doi/10.1145/1571941.1572114). In Proceedings of the 32nd international ACM SIGIR conference on Research and development in information retrieval (SIGIR '09). Association for Computing Machinery, New York, NY, USA, 758–759. <https://doi.org/10.1145/1571941.1572114>.

Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Singh Chaplot, D., de las Casas, D., … & El Sayed, W. (2023). [Mistral 7B](https://arxiv.org/abs/2310.06825). arXiv e-prints, arXiv-2310. <https://doi.org/10.48550/arXiv.2310.06825>.

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., … & Kiela, D. (2020). [Retrieval-augmented generation for knowledge-intensive nlp tasks](https://arxiv.org/abs/2005.11401). Advances in Neural Information Processing Systems, 33, 9459–9474.

Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). [Lost in the middle: How language models use long contexts](https://arxiv.org/abs/2307.03172). Transactions of the Association for Computational Linguistics, 12, 157–173.

Robertson, S., & Zaragoza, H. (2009). [The probabilistic relevance framework: BM25 and beyond](https://dl.acm.org/doi/10.1561/1500000019). Foundations and Trends® in Information Retrieval, 3(4), 333–389. <https://doi.org/10.1561/1500000019>

Thibault Formal, Benjamin Piwowarski, and Stéphane Clinchant. 2021. [SPLADE: Sparse Lexical and Expansion Model for First Stage Ranking](https://dl.acm.org/doi/10.1145/3404835.3463098). In Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '21). Association for Computing Machinery, New York, NY, USA, 2288–2292. <https://doi.org/10.1145/3404835.3463098>.

Tunstall, L., Beeching, E., Lambert, N., Rajani, N., Rasul, K., Belkada, Y., … & Wolf, T. (2023). Zephyr: Direct Distillation of LM Alignment. arXiv e-prints, arXiv-2310. <https://doi.org/10.48550/arXiv.2310.16944>.

## Misc Notes

- There is an issue with newer langchain package versions and streamlit chat history, see https://github.com/langchain-ai/langchain/pull/18834
  - This one reason why a number of dependencies are pinned to specific values.
>>>>>>> 83d150474fd50d8dae19df2ecf2b57c061bfa497
