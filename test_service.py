import unittest
import requests
import logging

# Настройка логирования
logging.basicConfig(
    filename="test_service.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class TestRecommendationService(unittest.TestCase):
    recommendations_url = "http://127.0.0.1:8000"
    events_store_url = "http://127.0.0.1:8020"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    # Тестовые данные
    user_id_no_personal = 8888888888888888
    user_id_personal_no_online = 1
    user_id_personal_with_online = 2
    event_item_ids = [26, 38, 135, 138]
    
    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом."""
        # Добавляем онлайн-историю для пользователя с персональными рекомендациями
        for item_id in self.event_item_ids:
            response = requests.post(
                self.events_store_url + "/put",
                headers=self.headers,
                params={"user_id": self.user_id_personal_with_online, "item_id": item_id}
            )
            self.assertEqual(response.status_code, 200)
    
    def tearDown(self):
        """Очистка после каждого теста (если необходима)."""
        pass
    
    def log_recommendations(self, test_case, recs_offline, recs_online, recs_blended):
        """Логирует результаты рекомендаций."""
        logging.info(f"=== {test_case} ===")
        logging.info(f"Офлайн: {recs_offline}")
        logging.info(f"Онлайн: {recs_online}")
        logging.info(f"Перемешанные: {recs_blended}")
        logging.info("=====================")
    
    def test_user_without_personal_recommendations(self):
        """Тест 1: Пользователь без персональных рекомендаций."""
        params = {"user_id": self.user_id_no_personal, 'k': 10}
        
        # Запросы к сервису рекомендаций
        resp_offline = requests.post(
            self.recommendations_url + "/recommendations_offline",
            headers=self.headers,
            params=params
        )
        resp_online = requests.post(
            self.recommendations_url + "/recommendations_online",
            headers=self.headers,
            params=params
        )
        resp_blended = requests.post(
            self.recommendations_url + "/recommendations",
            headers=self.headers,
            params=params
        )
        
        # Проверка статус-кодов
        self.assertEqual(resp_offline.status_code, 200)
        self.assertEqual(resp_online.status_code, 200)
        self.assertEqual(resp_blended.status_code, 200)
        
        # Проверка структуры ответа
        recs_offline = resp_offline.json()
        recs_online = resp_online.json()
        recs_blended = resp_blended.json()
        
        self.assertIn("recs", recs_offline)
        self.assertIn("recs", recs_online)
        self.assertIn("recs", recs_blended)
        
        # Логирование результатов
        self.log_recommendations(
            "Тест 1: Пользователь без персональных рекомендаций",
            recs_offline["recs"],
            recs_online["recs"],
            recs_blended["recs"]
        )
    
    def test_user_with_personal_recommendations_no_online_history(self):
        """Тест 2: Пользователь с персональными рекомендациями, но без онлайн-истории."""
        params = {"user_id": self.user_id_personal_no_online, 'k': 10}
        
        # Запросы к сервису рекомендаций
        resp_offline = requests.post(
            self.recommendations_url + "/recommendations_offline",
            headers=self.headers,
            params=params
        )
        resp_online = requests.post(
            self.recommendations_url + "/recommendations_online",
            headers=self.headers,
            params=params
        )
        resp_blended = requests.post(
            self.recommendations_url + "/recommendations",
            headers=self.headers,
            params=params
        )
        
        # Проверка статус-кодов
        self.assertEqual(resp_offline.status_code, 200)
        self.assertEqual(resp_online.status_code, 200)
        self.assertEqual(resp_blended.status_code, 200)
        
        # Проверка структуры ответа
        recs_offline = resp_offline.json()
        recs_online = resp_online.json()
        recs_blended = resp_blended.json()
        
        self.assertIn("recs", recs_offline)
        self.assertIn("recs", recs_online)
        self.assertIn("recs", recs_blended)
        
        # Логирование результатов
        self.log_recommendations(
            "Тест 2: Пользователь с персональными рекомендациями, но без онлайн-истории",
            recs_offline["recs"],
            recs_online["recs"],
            recs_blended["recs"]
        )
    
    def test_user_with_personal_recommendations_and_online_history(self):
        """Тест 3: Пользователь с персональными рекомендациями и онлайн-историей."""
        params = {"user_id": self.user_id_personal_with_online, 'k': 10}
        
        # Запросы к сервису рекомендаций
        resp_offline = requests.post(
            self.recommendations_url + "/recommendations_offline",
            headers=self.headers,
            params=params
        )
        resp_online = requests.post(
            self.recommendations_url + "/recommendations_online",
            headers=self.headers,
            params=params
        )
        resp_blended = requests.post(
            self.recommendations_url + "/recommendations",
            headers=self.headers,
            params=params
        )
        
        # Проверка статус-кодов
        self.assertEqual(resp_offline.status_code, 200)
        self.assertEqual(resp_online.status_code, 200)
        self.assertEqual(resp_blended.status_code, 200)
        
        # Проверка структуры ответа
        recs_offline = resp_offline.json()
        recs_online = resp_online.json()
        recs_blended = resp_blended.json()
        
        self.assertIn("recs", recs_offline)
        self.assertIn("recs", recs_online)
        self.assertIn("recs", recs_blended)
        
        # Логирование результатов
        self.log_recommendations(
            "Тест 3: Пользователь с персональными рекомендациями и онлайн-историей",
            recs_offline["recs"],
            recs_online["recs"],
            recs_blended["recs"]
        )

if __name__ == '__main__':
    unittest.main()