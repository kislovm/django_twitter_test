# coding: utf-8

import tweepy
from tweepy import Cursor



class timeline():
    
    timeline = []

    def __init__(self, screen_name):
        #auth = tweepy.OAuthHandler('cgG6YUitlpof3M4mpamIg', 'wV9N6FDh7USQO5VzvIJRbCqrhH4nw6511SWxEhSacM')
        #auth.set_access_token('57903901-8MS4j9Pb3nenaKGV3CvZP8Pu9ocwOqV6JK1jAobTL', '7Leu3whjGtfLzWfJXDGyHeJscOPVf5bTkehx5ZZyDzc')
        self.api = tweepy.API()
        for status in Cursor(self.api.user_timeline, screen_name=screen_name).items():
            status = self.getMentions(status) 
            self.timeline.append( status )
    
    def getMentions(self, status):
        mentions = []
        results = self.api.related_results(status.id)
        if len(results) > 0:
            results = results[0].results
            for result in results:
                tmp = result.value
                if tmp.in_reply_to_status_id == status.id:
                    tmp = self.getMentions(tmp)
                    mentions.append(tmp)
        return( [status, mentions, ] )
