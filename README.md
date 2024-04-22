# ParaCLIP

This is the official repository for [**ParaCLIP**](https://aclanthology.org/2024.findings-eacl.144/), a new CLIP model designed for robust multi-modal retrieval.

* 🤔 **Problem**: Current CLIP models often struggle with linguistic variations in input queries, such as paraphrases, leading to inconsistent image retrieval results for queries with similar meanings.

* 🚀 **What is ParaCLIP**: ParaCLIP enhances the text encoder of standard CLIP models to be more robust against variations in language semantics and composition. It shows significant improvements over baseline CLIP models across various tasks, including paraphrased retrieval (with rank similarity scores improved by up to 2.0% and 5.6%), compositional understanding tasks, and semantic textual similarity (STS) tasks. Additionally, it boosts performance in the text retrieval task on the COCO dataset.

* 🔍 **Training Method**: We created 5M synthetic paraphrases of original image captions (sourced from LAION-400M) and fine-tuned the text encoder using contrastive learning while keeping the image encoder fixed.

* 📄 **Paper**: [Fine-tuning CLIP Text Encoders with Two-step Paraphrasing
](https://aclanthology.org/2024.findings-eacl.144/)

* 👨‍💻 **Team**: This research was a collaborative effort between the [DMIS Lab](https://dmis.korea.ac.kr/) at Korea University and [Adobe Research](https://research.adobe.com/).

## Environments

```
conda create -n paraclip python=3.9 -y
conda activate paraclip
conda install pytorch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 pytorch-cuda=11.8 -c pytorch -c nvidia -y
pip install -r requirements.txt
```

## Usage
Our models are built upon the [OpenCLIP]([https://2022.emnlp.org/](https://github.com/mlfoundations/open_clip)) model structure. See the example in the `notebooks` folder to learn how to load our models.

### Model Weights
Please reach out to us via [email](#contact).

## Paraphrase Generation
Please check the `paraphrasing` folder if you want to generate paraphrased data from scratch.

## References

Please cite our paper ([**EACL 2024**](https://2024.eacl.org/), Findings) if our work is relevant to yours or has been helpful. Thank you!

```bibtex
@inproceedings{kim-etal-2024-fine,
    title = "Fine-tuning {CLIP} Text Encoders with Two-step Paraphrasing",
    author = "Kim, Hyunjae  and
      Yoon, Seunghyun  and
      Bui, Trung  and
      Zhao, Handong  and
      Tran, Quan  and
      Dernoncourt, Franck  and
      Kang, Jaewoo",
    editor = "Graham, Yvette  and
      Purver, Matthew",
    booktitle = "Findings of the Association for Computational Linguistics: EACL 2024",
    month = mar,
    year = "2024",
    address = "St. Julian{'}s, Malta",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-eacl.144",
    pages = "2175--2184",
}
```

## Contact

Feel free to email Hyunjae Kim (`hyunjae-kim@korea.ac.kr`) and David Seunghyun Yoon (`mysmilesh@gmail.com`) if you have any questions.

## License

Our models were trained using data generated through the OpenAI API and are therefore available only for non-commercial use and research purposes. See the `LICENSE` file for details.
