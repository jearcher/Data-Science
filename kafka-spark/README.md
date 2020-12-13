# Kafka and Spark project

### hypothetical situation:
I work at an ed tech firm that has created a service that
delivers assessments, and now lots of different customers (e.g., Pearson) want
to publish their assessments on it. We need to get ready for data scientists
who work for these customers to run queries on the data. 

### Summary of tasks

Prepare the infrastructure to land the data in the form and structure it needs
to be to be queried:

- Publish and consume messages with Kafka
- Use Spark in a Jupyter notebook to transform the messages. 
- Use Spark in a Jupyter notebook to transform the messages so that you can land them in HDFS


### The Data

Data pulled from:

```
curl -L -o assessment-attempts-20180128-121051-nested.json https://goo.gl/ME6hjp`
```

