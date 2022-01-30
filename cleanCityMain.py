from __future__ import print_function

import datetime
import os.path

from flask import Flask, url_for, render_template, redirect

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


neighList = {
    "neighborhood1" : "Pittsburgh",
    "neighborhood2" : "Philidelphia",
    "neighborhood3" : "Harrisburg",
    "neighborhood4" : "Erie"
}

personList = {
    "John" : 500,
    "Alice" : 450,
    "Emily" : 440,
    "Mike" : 400
}

#git push --set-upstream origin main
@app.route("/neighborhoodScore")
def show_neighScore():
    return render_template("neighScore.html", topNeighList = neighList)

@app.route("/home")
def show_home():
    return render_template("home.html")

@app.route("/individualCleaning")
def show_individualClean():
    return render_template("indivClean.html")

@app.route("/cleaningEvent")
def show_cleaningEvents():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=63551)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        #print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=6, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        #Prints the start and name of the next 10 events
        
        eventsListToPass = []
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            creator = event['creator'].get('email')
            temp = {
                "summary": event['summary'],
                "start" : start,
                "end" : end,
                "creator": creator
            }
            eventsListToPass.append(temp)
            

    except HttpError as error:
        print('An error occurred: %s' % error)

    return render_template("cleaningEvent.html", theEvents = eventsListToPass)

@app.route("/about")
def show_about():
      return render_template("about.html")

@app.route("/contact")
def show_contact():
      return render_template("contact.html")

@app.route("/prizes")
def show_prizes():
    return render_template("prize.html")

@app.route("/indivScore")
def show_indivScore():
    return render_template("indivScore.html", topContr = personList)

app.run()