# Identification of Promotional Content on Instagram
Team Member 1: Kayli Leung

Team Member 2: Sherry Yang

[Presentation]()

## Business Understanding
Instagram has been the location in which many people have earned money via their posts. Instagram has more social influencers than any other social media network. Instagram and other company's want to be able to identify influencers to help their ad revenue. We seek to identify the "promotional-ness" of a post by its comment and not it's picture. 

## Data Understanding
We scraped 50 public instagram users using selenium. We used a selection of celebrities, politicians, known influencers, companies, and other public profiles to collect our data. For analysis we collected only the initial comment by the poster, which we will call the caption.

## Data Preparation
We hand labeled our data as promotional or non-promotional. We determined a general set of rules for our labeling purposes. If a post is a direct call to do something (buy, check out, vote, come) it is promotional. It may also be promotional if it tags/links to a company. This may not always be the case and is determined on a case by case basis. When it comes to self-promotion, if the post represented a value or a belief, but no call to action then it is considered non-promotion. This was especially important to label the politician's posts. 

Note: We understand that we did not use DRY while we scraped and labeled the data. However, we wanted to show our process in which we did not yet know who we were scraping. 

[Notebook]()

## Modeling
We tokenized the captions using kera's tokenizer. We then used our tokenized captions in a shallow neural network. Our neural network featured an emmbedding layer and a bidirectional LSTM layer. After training on 1065 posts (using 10% as validation) we achieved our final model. 

[Notebook]()

## Evaluation
The model was evaluated on 248 unseen captions by unseen instagram users. The model had an accuracy of 70%. Admittedly, this is not the best accuracy, however, when we were hand labeling the data there was a lot of gray area in some of the captions.We also had some sampling bias as we used a very small proportion of instagram users.

We explored the captions that were incorrectly classified and noticed some trends in the error. First, the most common type of error was to predict non-promotional when the post was promotional. One possible reason, is that there was slightly more non-promotional captions in our training data. A second related trend is that for long posts that were promotional, if the promotional material was at the end of the caption, it was harder to classify as promotional than if it was at the beginning of the caption. Third, there were some misclassified post that had the literal word "ad" in the caption. It is possible that this word did not show up much, if at all in the training data and therefore it did not learn that ad was promotional.

[Notebook]()

## Deployment
We created a flask app so that you can determine if a caption is promotional or not. 

## Future Exploration
We had a very small sample of Instagram as we had limited time to scrape and label the data. We would like to have more data to construct a more representative model of captions. We would also like to check with more people about the labeling of our data. There was a lot of gray area when it came to labeling the data and having additional input would make our labels more similar to the ground truth. We could also fix this by creating more classes such as self-promotion, fundraiser, thank you, etc. We attempted to use BERT or ULMFiT as a pretrained model. However, we had some trouble implementing and downloading these models onto our machines. We would still like to use them in the future. 

## Citations:
[jnawjux for webscrapping](https://github.com/jnawjux/web_scraping_corgis)