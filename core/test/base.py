import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.db import Base
from app.users.services import UserService


class TestBaseService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the in-memory database and create tables
        cls.engine = create_engine("sqlite:///:memory:")
        cls.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls.engine)
        cls.session = cls.SessionLocal()
        Base.metadata.create_all(bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        # Drop all tables after tests
        Base.metadata.drop_all(bind=cls.engine)
        cls.session.close()

    def setUp(self):
        # Create a new session for each test
        self.session = self.SessionLocal()
        self.user_service = UserService(self.session)

    def tearDown(self):
        # Rollback any changes and close the session after each test
        self.session.rollback()
        self.session.close()
