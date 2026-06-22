
# analyzer.py

class ScreenAnalyzer:

    def __init__(self):

        self.app_categories = {

            "coding": [
                "code.exe",
                "pycharm64.exe",
                "devenv.exe",
                "cursor.exe"
            ],

            "browser": [
                "chrome.exe",
                "msedge.exe",
                "firefox.exe"
            ],

            "document_work": [
                "winword.exe"
            ],

            "spreadsheet_work": [
                "excel.exe"
            ],

            "presentation_work": [
                "powerpnt.exe"
            ],

            "file_management": [
                "explorer.exe"
            ]
        }

    # =====================================================
    # MAIN CONTEXT DETECTOR
    # =====================================================

    def detect_context(self, app_name, title=""):

        app_name = str(app_name).lower()
        title = str(title).lower()

        # -------------------------------------------------
        # ARTERY DEVELOPMENT
        # -------------------------------------------------

        if "artery" in title:

            return "artery_development"

        # -------------------------------------------------
        # CODING
        # -------------------------------------------------

        if app_name in self.app_categories["coding"]:

            if "github" in title:
                return "development_research"

            return "coding"

        # -------------------------------------------------
        # FILE MANAGEMENT
        # -------------------------------------------------

        if app_name == "explorer.exe":

            if "downloads" in title:
                return "download_management"

            if "documents" in title:
                return "document_management"

            if "pictures" in title:
                return "media_management"

            return "file_management"

        # -------------------------------------------------
        # DOCUMENTS
        # -------------------------------------------------

        if app_name == "winword.exe":

            return "document_work"

        if app_name == "excel.exe":

            return "spreadsheet_work"

        if app_name == "powerpnt.exe":

            return "presentation_work"

        # -------------------------------------------------
        # BROWSER INTELLIGENCE
        # -------------------------------------------------

        if app_name in self.app_categories["browser"]:

            # YouTube

            if "youtube" in title:
                return "media_consumption"

            # Gmail

            if "gmail" in title:
                return "email_management"

            # ChatGPT

            if "chatgpt" in title:
                return "ai_interaction"

            # GitHub

            if "github" in title:
                return "development_research"

            # LinkedIn

            if "linkedin" in title:
                return "professional_networking"

            # LeetCode

            if "leetcode" in title:
                return "coding_practice"

            # Stack Overflow

            if "stack overflow" in title:
                return "technical_research"

            # Google Docs

            if "docs.google" in title:
                return "document_work"

            # Google Sheets

            if "sheets.google" in title:
                return "spreadsheet_work"

            # Google Drive

            if "drive.google" in title:
                return "cloud_storage"

            return "web_browsing"

        # -------------------------------------------------
        # FALLBACK
        # -------------------------------------------------

        return "unknown"

    # =====================================================
    # ACTIVITY LEVEL
    # =====================================================

    def get_activity_level(self, context):

        high_focus = [
            "coding",
            "artery_development",
            "technical_research",
            "coding_practice"
        ]

        medium_focus = [
            "document_work",
            "spreadsheet_work",
            "presentation_work",
            "professional_networking"
        ]

        low_focus = [
            "media_consumption",
            "web_browsing"
        ]

        if context in high_focus:
            return "high"

        if context in medium_focus:
            return "medium"

        if context in low_focus:
            return "low"

        return "unknown"

