def test_signup_success_for_existing_activity(client):
    email = "new.student@mergington.edu"

    response = client.post("/activities/Chess%20Club/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}

    activities_response = client.get("/activities")
    assert email in activities_response.json()["Chess Club"]["participants"]


def test_signup_fails_when_student_already_signed_up(client):
    existing_email = "michael@mergington.edu"

    response = client.post(
        "/activities/Chess%20Club/signup", params={"email": existing_email}
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up"}


def test_signup_fails_for_unknown_activity(client):
    response = client.post(
        "/activities/Unknown%20Activity/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}
