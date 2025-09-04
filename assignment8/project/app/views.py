from django.http import HttpResponse
from django.views import View

# function-based view
def home(request):
    html = """
    <html>
    <head>
        <title>Home Page</title>
        <style>
            h1 {
                text-align: center;
                width: 12%;
                padding: 40px;
                margin: 60px auto;
                background-color: chocolate;
                border-radius: 8px;
                border: 5px solid brown;
                color: beige;
                text-shadow: 2px 2px 2px brown;
                animation: flash 1s infinite;
            }

            @keyframes flash {
                0% {
                    background-color: chocolate;
                    color: beige;
                }

                50% {
                    background-color: orange;
                    color: white;
                }

                100% {
                    background-color: chocolate;
                    color: beige;
                }
            }
        </style>
    </head>
    <body>
        <h1>Home Page</h1>
    </body>
    </html>
    """
    return HttpResponse(html)


# class-based view
class NotFound(View):
    def get(self, request):
        html = """
        <html>
        <head>
            <title>404 - გვერდი არ არსებობს</title>
            <style>
                body {
                    background-color: #f8f8f8;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                }

                .error-box {
                    display: inline-block;
                    padding: 40px;
                    border: 5px solid #e74c3c;
                    border-radius: 10px;
                    background-color: #fff;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
                    animation: pulse 2s infinite;
                }

                h1 {
                    font-size: 48px;
                    color: #e74c3c;
                    margin-bottom: 10px;
                }

                p {
                    font-size: 18px;
                    color: #555;
                }

                @keyframes pulse {
                    0% {
                        transform: scale(1);
                    }
                    50% {
                        transform: scale(1.05);
                    }
                    100% {
                        transform: scale(1);
                    }
                }
            </style>
        </head>
        <body>
            <div class="error-box">
                <h1>404</h1>
                <p>გვერდი არ არსებობს :(</p>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html, status=404)


