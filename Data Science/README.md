# Data Science [Address Elements Extraction] - Shopee Code League 2021

[Source](https://www.kaggle.com/c/scl-2021-ds/overview)

### Task

- Build a model to correctly extract **Point of Interest (POI)** Names and Street Names from unformatted Indonesia adresses.

### Description Data
- train.csv : contains training dataset for the address elements extraction. Columns: [id, raw_adress, POI/street]

- test.csv : contains test dataset for the address elements extraction. Columns: [id, raw_adress]

- sampleSubmission.csv : contains sample submission

### Example Submission

| Id      | POI/street |
| ----------- | ----------- |
| 0     | /       |
| 1   | pt tunas arthagardatama/lenteng agung barat        |
| 2     | /lenteng agung barat  |
| 3     | muh sigit wahyu p dr sp kj/jalan adi sucipto      |
| 4     | senam melinda/        |

Submission must have **50.000 rows**, each with 2 columns.


### Referensi 
- https://becominghuman.ai/part-of-speech-tagging-tutorial-with-the-keras-deep-learning-library-d7f93fa05537
- https://towardsdatascience.com/addressnet-how-to-build-a-robust-street-address-parser-using-a-recurrent-neural-network-518d97b9aebd
- https://machinelearnings.co/statistical-nlp-on-openstreetmap-b9d573e6cc86
- https://medium.com/@albarrentine/statistical-nlp-on-openstreetmap-part-2-80405b988718
- https://github.com/openvenues/libpostal