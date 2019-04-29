 <img src="https://raw.githubusercontent.com/code-for-venezuela/2019-april-codeathon/master/assets/medicosporlasalud.jpg" alt="Medicos por la Salud" width="80" />

# Using Twitter Data to Help Public Health

## TL;DR

The ultimate goal of this challenge is to create predictive models using Twitter data to:
1. Detect epidemic outbreaks.
2. Identify where a particular medicine is needed in the country.

**NOTE: We don't expect this challenge to be completed during the Hackathon, the goal is to set the foundational work that will allow us to solve this problem.**

## Background

### Who we are

**About Dr. Julio Castro**

Dr. Julio Castro is a Venezuelan doctor and professor specializing in infectious diseases. He is one of the most important activists focusing on the public health sector. Since 2014, when the official data was Dr. Castro and his team gather health statistics using a digital tool that allows them to monitor hospitals across the country.

His work has been widely covered in both national and international media:

*   [https://www.ozy.com/rising-stars/the-great-zika-cover-up/70901](https://www.ozy.com/rising-stars/the-great-zika-cover-up/70901)
*   [https://www.univision.com/univision-news/latin-america/for-doctors-in-venezuela-the-simplest-disease-can-become-a-tragedy](https://www.univision.com/univision-news/latin-america/for-doctors-in-venezuela-the-simplest-disease-can-become-a-tragedy)

**About Medicos por la Salud**

_Medicos por la Salud_ is a network of doctors distributed across the country that has been monitoring hospitals and publishing a yearly report ([Encuesta Nacional de Hospitales](https://www.encuestanacionaldehospitales.com/)) that tries to quantify and communicate the magnitude of the public health crisis in Venezuela.

## Problem Statement

Venezuela has seen an unprecedented increase in cases of malaria, measles, diphtheria and zika.

_References_

[Infectious Diseases Spike amid Venezuela's Political Turmoil](https://www.scientificamerican.com/article/infectious-diseases-spike-amid-venezuelas-political-turmoil/)

[Venezuela crisis threatens disease epidemic across continent - experts](https://www.theguardian.com/global-development/2019/feb/21/venezuela-crisis-threatens-disease-epidemic-across-continent-experts)

On top of this, medicine scarcity is one of the most severe problems that Venezuela faces today. Hospitals can go without essential medications like adrenaline, insulin, and anesthetics for months at a time.

Dr. Julio Castro and his team have been conducting surveys in hospitals nationwide to keep track of where specific medications are most needed. They have also been collecting a database of more than 1 million tweets that contain medical supply requests, emergency data, and other indicators.

They believe this data, combined, may be used for the following:

1. Making informed decisions on where to deploy limited quantities of specific medications brought as humanitarian aid.
2. Detecting disease outbreaks in real-time. These reports would otherwise take weeks to go through the official channels, making it really hard to react to the outbreaks, which costs many lives in the process.

## Challenge

Dr. Julio Castro has shared the Twitter data they have been collecting. Code For Venezuela has done an initial analysis of this data. Below you can find the results of that study to give you some context about the problem.

### Data Summary

We have a little bit over 1M tweets containing hashtags related to [#ServicioPublico](https://twitter.com/hashtag/ServicioP%C3%BAblico?src=hash), which is a popular hashtag used in Venezuela whenever a specific medicine or medical treatment is being searched by Venezuelans. It provides a way to connect people who need to find specific medicines with people in different parts of the country that might have access to that medicine.


<table>
  <tr>
   <td><strong>Field Name</strong>
   </td>
   <td><strong>Field Description</strong>
   </td>
  </tr>
  <tr>
   <td>tweet_date
   </td>
   <td>Time when the tweet was created in Pacific Timezone.
   </td>
  </tr>
  <tr>
   <td>tweet_text
   </td>
   <td>Content of the tweet.
   </td>
  </tr>
  <tr>
   <td>tweet_url
   </td>
   <td>Link to this tweet on <a href="https://twitter.com/">twitter.com</a>.
   </td>
  </tr>
  <tr>
   <td>hash_tags
   </td>
   <td>List of hash tags present on the tweet (computed by us by parsing the tweet).
   </td>
  </tr>
  <tr>
   <td>raw_tweet
   </td>
   <td>Raw HTML gotten when the tweet was originally ingested.
   </td>
  </tr>
</table>

Raw data is available [here](https://drive.google.com/open?id=1Y0dA_EaNPOmEyCaJC_0qtx5i9P4Ykz8m).



### Data Limitations

We found the following issues with the data:

*   Data might be incomplete. According to the Twitter API descriptions, we believe that the data ingested by Dr. Castro might be only a sample of the data from the hashtag specified above. This is because you need access to the Enterprise or Premium APIs to get all tweets matching a specific query instead of a sample of them.
*   There are duplicates in this data, meaning that popular tweets will be over-represented.
*   We don't have any labeled data that we could use to correlate these tweets to, for example, outbreak diseases.

This should be problems that could be handled during the hackathon by different teams.

**We are trying to explore possible ways to get access to Twitter premium APIs, but this is currently a work in progress. If we do get access to it, participants could leverage the Twitter Historical API and the metadata that comes with it to work on this problem**

### Proposed Challenges

Due to the issues highlighted above, we are proposing the following set of challenges that use and are inspired by this data:

#### 1. **Data Ingestion Pipeline**

Create a data pipeline that would keep ingesting these tweets and that can potentially use Twitter's premium APIs to keep an up to date stream of [#ServicioPublico](https://twitter.com/hashtag/ServicioP%C3%BAblico?src=hash) tweets.

This pipeline should provide a reliable way of ingesting Twitter data for `#ServicioPublico` and ideally should provide a way to find whenever any issues arise during ingestion.


#### 2. Data set enrichment

The data in its current state does not have enough information to create predictive models so we need to extend it and analyze it. Here are some ideas in this direction:

* **Tweet De-duplication**: as a first step, how do we remove duplicated tweets so that posterior analysis are not misleading due to some popular tweets.
* **Change Point Detection**: use [Change Point Detection](https://en.wikipedia.org/wiki/Change_detection) to determine times when these tweets suddenly become more common.
* **NLP analysis**: Build a tool/pipeline that, given the data from Twitter, can understand whether a specific tweet is requesting a specific medicine so that identical medicines can be grouped together. This would require using NLP on tweets in Spanish.

A possible outcome of NLP could be providing descriptive statistics of medicine requests vs others (beds, materials, electricity).
* **Geolocate the Tweet**: At the moment, tweets do not have geolocation data. Can you find ways to get this information (e.g querying Twitter API, inferring location by detecting locations or users, etc)
* **Medicine to disease mapping**: Once we get information about medicines in a tweet, we will need to create training data set that maps those tweets to diseases that are cured with those medicines.

#### 3. **Data Visualization**

Visualize the data given to see whether some patterns emerge over time. One motivating question would be: which medicines are requested more often during specific times?

Visualization can aid in detecting points in time where the number of tweets requesting medicine and or medical equipment has significantly changed.

#### 4. Predictive Models

Once the data is curated and traditional ML techniques can be applied to it, the ultimate goal of this project is to create predictive models that using Twitter data to:

1. Detect epidemic outbreaks.
2. Identify where a particular medicine is needed in the country.


**NOTE: Projects 1, 2, 3 are orthogonal and you don't need to solve them all. They could be split between different teams in the Hackathon. Project 4 is aspirational and depends on 2.**

## Skills Required

1. Data engineering
2. Google Cloud storage
3. Column Data Store
4. Airflow
5. Machine Learning
6. NLP

## Project contact
Dr. Julio Castro, [@juliocastrom](https://twitter.com/juliocastrom)
