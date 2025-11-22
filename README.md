# 🧬 Multi-Class Cancer Classification via Deep Learning
A comprehensive deep learning project aimed at accurate multi-class cancer detection using advanced CNN and Transformer-based architectures.
This repository includes model training pipelines, evaluation metrics, comparative analysis, and future work for real-world deployment.

# 🚀 Models Implemented
A diverse set of CNN and Transformer-based architectures were implemented and evaluated:
- VGG16
- DenseNet201
- InceptionV3
- Data-Efficient Image Transformer
- Mobile Vision Transformer (MobileViT)
- Residual Vision Transformer (ResViT)
- Multiscale Vision Transformer
- BERT + Image Transformer Hybrid Model

Each model was trained, tuned, and tested to obtain reliable baseline results.

# 📊 Results (Accuracy & Metrics)
| Model                               | Accuracy | Precision | Recall | F1-Score |
|-------------------------------------|----------|-----------|--------|----------|
| VGG16                               | 97.54%   | 97.95     | 98.05  | 98.00    |
| Data-efficient Image Transformer    | 98.26%   | 99.02     | 99.00  | 99.00    |
| DenseNet201                         | 99.93%   | 99.93     | 99.93  | 99.93    |
| Mobile Vision Transformer           | 99.69%   | 99.74     | 99.74  | 99.74    |
| Residual Vision Transformer (ResViT)| 97.54%   | 98.54     | 97.99  | 97.99    |
| InceptionV3                         | 97.40%   | 97.90     | 97.87  | 97.90    |
| Multiscale Vision Transformer       | 94.81%   | 94.97     | 94.81  | 94.84    |
| BERT + Image Transformer            | 99.50%   | 99.58     | 99.63  | 99.61    |

🏆 Best Performer: DenseNet201 (99.93% Accuracy)

# 🛠️ Key Features
Comprehensive comparison of CNN vs Transformer architectures
- High-performance multi-class classification
- Scalable training and evaluation pipeline
- Integration of hybrid text-image (BERT + ViT) approaches
- Organized documentation of results & observations


# 📝 Conclusion
- Achieved up to 99.93% accuracy using DenseNet201, with strong performance across multiple architectures.
- Demonstrated importance of model choice depending on cancer type and dataset characteristics.
- Established groundwork for a deployable automated diagnostic tool.
- Future improvements focus on usability, robustness, and interpretability for real-world adoption.
