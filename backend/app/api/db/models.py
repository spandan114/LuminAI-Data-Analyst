# File: app/db/models.py
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Enum, DateTime, ForeignKey, Text, text
from app.config.env import DATABASE_URL
import logging
from .user import User
from .data_sources import DataSources

logger = logging.getLogger(__name__)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)
meta = MetaData()

# Define tables
users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("email", String(100), unique=True),
    Column("hashed_password", String(400), unique=True),
    Column("created_at", DateTime, server_default=text('CURRENT_TIMESTAMP'))
)

data_sources = Table(
    "data_sources",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("name", String(50)),
    Column("type", String(50)),
    Column("table_name", String(400), nullable=True, unique=True),
    Column("connection_url", String(400), nullable=True, unique=True),
    Column("created_at", DateTime, server_default=text('CURRENT_TIMESTAMP'))
)

# Conversations table - stores high-level conversation sessions
conversations = Table(
    "conversations",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    # Auto-generated title or first message snippet
    Column("title", String(200)),
    Column("created_at", DateTime, server_default=text('CURRENT_TIMESTAMP')),
    Column("updated_at", DateTime, server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP')),
    Column("status", Enum('active', 'archived', 'deleted',
           name='conversation_status'), default='active'),
)

# Messages table - stores individual messages in conversations
messages = Table(
    "messages",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("conversation_id", Integer, ForeignKey("conversations.id")),
    Column("role", Enum('user', 'assistant', 'system', name='message_role')),
    Column("content", Text),  # The actual message content
    Column("created_at", DateTime, server_default=text('CURRENT_TIMESTAMP')),
    Column("updated_at", DateTime, server_default=text(
        'CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP')),
    Column("tokens_used", Integer),  # Optional: track token usage
)


def init_db():
    try:
        # This will create both the enum type and tables
        meta.create_all(engine)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise
