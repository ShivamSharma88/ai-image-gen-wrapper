#!/usr/bin/env python3
"""
Main entry point for the AI Image Generation Wrapper application.
"""

import uvicorn
import logging
import sys
from pathlib import Path
from dotenv import load_dotenv
import os

# Add app directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from app.main import create_app
from app.config import settings

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting AI Image Generation Wrapper...")
    logger.info(f"API running on {settings.API_HOST}:{settings.API_PORT}")
    logger.info(f"Debug mode: {settings.DEBUG}")
    logger.info(f"Training device: {settings.TRAINING_DEVICE}")
    
    # Create FastAPI app
    app = create_app()
    
    # Run server
    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
