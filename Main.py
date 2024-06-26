import Mysql
from datetime import datetime
import smtplib



def send_simple_email(sender_email,sender_password,recipient_mail,subject,body):
    email_message = f"Subject: {subject}\n\n{body}"
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_mail, email_message)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def user_():

    movies = {
        1: "Inception",
        2: "The Matrix",
        3: "Interstellar",
        4: "Avengers: Endgame"
    }

    prices = {

        "Inception":130,
        "The Matrix":200,
        "Interstellar":300,
        "Avengers Endgame":250
    }
    user_name = input("Enter Your Name: ")
    Mail_id = input("Enter Your Mail Id: ")

    print("Available Movies")
    for ind,movie in movies.items():
        print(f"{ind}. {movie}")

    try:
        choose = int(input("Which movie do you want to book: "))

        if choose in movies:
            select_movie = movies[choose]
            movie_price = prices[select_movie]
            print(f"Your have selected Movies: {select_movie}")

            print(calculation_amount(movie_price))

            Mysql.insert_data(user_name,select_movie,Mail_id)

            subject = "Your Movie Ticket"
            data_to_write = f"""
            Name: {user_name}
            Email: {Mail_id}
            Movie: {select_movie}
            Price: {movie_price}
            Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            -------------------------
            """

            try:
                with open("data.txt", "a") as file:  # Open the file in append mode
                    file.write(data_to_write)
                print("Booking details saved to file.")
            except Exception as err:
                print(f"Error writing to file: {err}")

            # Send the ticket to user's email
            sender_email = "praneshpranesh648@gmail.com"
            sender_password = "qoaa vssn sxoo rptq"
            send_simple_email(sender_email, sender_password, Mail_id, subject, data_to_write)

            print("Booking Successfuly")
        else:
            print("Invalid Choose")

    except ValueError:
        print("Invalid input please enter a number.")

def calculation_amount(price):
    gst = 0.18

    amount_without_gst = price 
    gst_amount = amount_without_gst * gst
    total_amount = amount_without_gst + gst_amount

    return total_amount

if __name__ == "__main__":
    user_()