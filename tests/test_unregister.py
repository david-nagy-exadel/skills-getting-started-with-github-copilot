def test_unregister_success_for_signed_up_student(client):
    email = "liam@mergington.edu"

    response = client.delete("/activities/Debate%20Team/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from Debate Team"}

    activities_response = client.get("/activities")
    assert email not in activities_response.json()["Debate Team"]["participants"]


def test_unregister_fails_for_student_not_signed_up(client):
    response = client.delete(
        "/activities/Art%20Studio/signup", params={"email": "not-enrolled@mergington.edu"}
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not signed up"}


def test_unregister_fails_for_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown%20Activity/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}
