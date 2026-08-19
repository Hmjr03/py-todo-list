from django.test import TestCase
from django.urls import reverse

from todo.models import Tag, Task


class TaskModelTests(TestCase):
    def test_task_is_created_with_default_not_done_status(self):
        task = Task.objects.create(
            content="Test task",
        )

        self.assertFalse(task.is_done)

    def test_task_can_have_tags(self):
        task = Task.objects.create(
            content="Tagged task",
        )
        tag = Tag.objects.create(
            name="work",
        )

        task.tags.add(tag)

        self.assertIn(tag, task.tags.all())


class TagModelTests(TestCase):
    def test_tag_string_representation(self):
        tag = Tag.objects.create(
            name="home",
        )

        self.assertEqual(str(tag), "home")


class TaskViewsTests(TestCase):
    def test_task_list_page_loads(self):
        response = self.client.get(
            reverse("task-list"),
        )

        self.assertEqual(response.status_code, 200)

    def test_task_create_page_loads(self):
        response = self.client.get(
            reverse("task-create"),
        )

        self.assertEqual(response.status_code, 200)

    def test_tag_list_page_loads(self):
        response = self.client.get(
            reverse("tag-list"),
        )

        self.assertEqual(response.status_code, 200)

    def test_task_can_be_toggled(self):
        task = Task.objects.create(
            content="Toggle task",
        )

        response = self.client.get(
            reverse(
                "task-toggle",
                kwargs={"pk": task.pk},
            )
        )

        task.refresh_from_db()

        self.assertTrue(task.is_done)
        self.assertRedirects(
            response,
            reverse("task-list"),
        )
