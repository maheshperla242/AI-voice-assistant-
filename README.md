To create a voice-controlled AI assistant that listens to user commands, responds via speech, and performs tasks like opening websites, searching Google, or fetching information from Wikipedia.

How the Project Works (Step by Step):

Activation (Wake Word)

The assistant waits for you to say the wake word: "January".

Once detected, it responds "Yes Boss" and starts listening for commands.

Speech Recognition

Uses the speech_recognition library.

Listens through the microphone and converts your voice into text using Google’s speech recognition API.

Handles background noise with adjust_for_ambient_noise() and threshold settings.

Processing Commands

After converting speech to text, your command is checked in the myCommand() function.

Commands are categorized into:

Open websites: YouTube, Instagram, GitHub, LinkedIn, Moodle.

Search online: Google search.

Information retrieval: Wikipedia summaries.

Exit command: To stop the assistant.

Text-to-Speech (TTS)

Uses pyttsx3 for offline speech synthesis.

Reads out responses to the user.

No temporary files needed (unlike gTTS + playsound), so no errors or delays.

Performing Actions

For website commands → opens the corresponding URL in the default browser using webbrowser.open().

For information commands → fetches a 2-sentence summary from Wikipedia and speaks it.

For Google search → opens the search results for the topic you specify.

Continuous Listening

Runs in a loop, so you can keep giving commands until you say "exit" or "quit".

Handles exceptions gracefully so it doesn’t crash if it doesn’t understand input.

Technologies Used:

Python – main programming language.

speech_recognition – converts speech to text.

pyttsx3 – converts text to speech offline.

webbrowser – to open websites automatically.

wikipedia – to fetch summaries of topics.

sys – to exit the program.

Key Highlights:

Offline text-to-speech (pyttsx3) avoids MP3/playback issues.

Real-time voice interaction makes it interactive and user-friendly.

Easy to expand with more commands like music, weather, or app control.

Lightweight – works on a normal computer without heavy resources.

If someone asks “How did you make it?”, you can say something like:

“I built a Python-based AI assistant using speech_recognition for voice input and pyttsx3 for voice output. It listens for a wake word, interprets commands like opening websites or searching Google, and responds in real-time. I also integrated Wikipedia to provide information summaries.”
