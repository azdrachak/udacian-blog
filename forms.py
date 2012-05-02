__author__ = 'Aliaksandr_Zdrachak'

form = """
<form method = "post">
    What is your birthday?
    <br>

    <label>
        Month
        <input type = "text" name = "month" value = "%(month)s">
    </label>

    <label>
        Day
        <input type = "text" name = "day" value = %(day)s>
    </label>

    <label>
        Year
        <input type = "text" name = "year" value = %(year)s>
    </label>
    <div style = "color: red">%(error)s</div>
    <br>
    <br>
    <input type = "Submit">
</form>
"""

form_encrypt = """
<form method = "post">
    <label>
        <strong><h2>ROT-13 encryption:</h2></strong>
        <textarea name = "text" rows = "20" cols = "50">%(data)s</textarea>
    </label>
    <br>
    <input type = "Submit" value = "Encrypt">
</form>
"""

#form_signup = """
#<!DOCTYPE html>
#
#<html>
#  <head>
#    <title>Sign Up</title>
#    <style type="text/css">
#      .label {text-align: right}
#      .error {color: red}
#    </style>
#
#  </head>
#
#  <body>
#    <h2>Signup</h2>
#    <form method="post">
#      <table>
#        <tr>
#          <td class="label">
#            Username
#          </td>
#          <td>
#            <input type="text" name="username" value="%(username)s">
#          </td>
#          <td class="error">
#            %(error_username)s
#          </td>
#        </tr>
#
#        <tr>
#          <td class="label">
#            Password
#          </td>
#          <td>
#            <input type="password" name="password" value="%(password)s">
#          </td>
#          <td class="error">
#            %(error_password)s
#          </td>
#        </tr>
#
#        <tr>
#          <td class="label">
#            Verify Password
#          </td>
#          <td>
#            <input type="password" name="verify" value="%(verify)s">
#          </td>
#          <td class="error">
#            %(error_verify)s
#          </td>
#        </tr>
#
#        <tr>
#          <td class="label">
#            Email (optional)
#          </td>
#          <td>
#            <input type="text" name="email" value="%(email)s">
#          </td>
#          <td class="error">
#            %(error_email)s
#          </td>
#        </tr>
#      </table>
#
#      <input type="submit">
#    </form>
#  </body>
#
#</html>
#"""