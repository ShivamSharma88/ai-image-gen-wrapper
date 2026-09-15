# AI Image Generation Wrapper

A comprehensive AI image generation wrapper that supports multiple API providers, self-training capabilities, custom skill uploads, and fine-tuning from user-provided datasets.

## Features

✨ **Multi-API Support**
- Support for multiple image generation APIs (OpenAI DALL-E, Stable Diffusion, Midjourney, etc.)
- Flexible API key management and switching
- Fallback mechanisms for API failures

🧠 **Self-Training & Fine-Tuning**
- Train models on custom datasets you provide
- Automatic model improvement through user feedback
- Dataset management and versioning
- Training metrics and performance tracking

🎯 **Skill System**
- Upload and manage custom skills/prompts
- Organize skills by category
- Version control for skills
- Community skill sharing (optional)

📊 **Data Management**
- Upload custom training datasets
- Support for multiple data formats (JSON, CSV, images)
- Data augmentation capabilities
- Training history and versioning

🔧 **Advanced Features**
- Model caching and optimization
- Batch image generation
- Result analytics and tracking
- API usage monitoring
- Webhook support for async operations

## Architecture

```
ai-image-gen-wrapper/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app setup
│   ├── config.py               # Configuration management
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── generate.py         # Image generation endpoints
│   │   ├── training.py         # Training & fine-tuning endpoints
│   │   ├── skills.py           # Skill management endpoints
│   │   ├── datasets.py         # Dataset management endpoints
│   │   └── auth.py             # Authentication endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   ├── schemas.py          # Pydantic models
│   │   ├── database.py         # Database models
│   │   └── training.py         # Training models
│   ├── services/
│   │   ├── __init__.py
│   │   ├── api_providers.py    # API integrations
│   │   ├── trainer.py          # Training service
│   │   ├── skill_manager.py    # Skill management
│   │   ├── dataset_manager.py  # Dataset management
│   │   └── cache_manager.py    # Caching layer
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py       # Input validation
│   │   ├── image_processing.py # Image utilities
│   │   ├── metrics.py          # Performance metrics
│   │   └── logger.py           # Logging setup
│   └── database/
│       ├── __init__.py
│       ├── connection.py       # DB connection
│       └── migrations.py       # Database migrations
├── models/
│   ├── base_model.pth          # Base trained models
│   └── checkpoints/
├── data/
│   ├── training_datasets/
│   ├── skills/
│   └── cache/
├── tests/
│   ├── __init__.py
│   ├── test_generation.py
│   ├── test_training.py
│   ├── test_skills.py
│   └── test_datasets.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── .env.example
├── main.py                     # Entry point
└── README.md
```

## Installation

### Prerequisites
- Python 3.9+
- CUDA 11.8+ (for GPU acceleration, optional)
- Docker (optional)

### Setup

```bash
# Clone the repository
git clone https://github.com/ShivamSharma88/ai-image-gen-wrapper.git
cd ai-image-gen-wrapper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Configure your API keys and settings in .env

# Run migrations
python -m alembic upgrade head

# Start the server
python main.py
```

### Docker Setup

```bash
docker-compose -f docker/docker-compose.yml up -d
```

## Quick Start

### 1. Configure API Keys

```bash
# .env file
OPENAI_API_KEY=sk-xxx
STABLE_DIFFUSION_API_KEY=xxx
MIDJOURNEY_API_KEY=xxx
```

### 2. Generate an Image

```bash
curl -X POST http://localhost:8000/api/v1/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A futuristic city at sunset",
    "provider": "openai",
    "model": "dall-e-3",
    "size": "1024x1024",
    "quality": "hd"
  }'
```

### 3. Upload Training Dataset

```bash
curl -X POST http://localhost:8000/api/v1/datasets/upload \
  -F "file=@training_data.json" \
  -F "dataset_name=my_dataset" \
  -F "description=Custom training data"
```

### 4. Start Training

```bash
curl -X POST http://localhost:8000/api/v1/training/start \
  -H "Content-Type: application/json" \
  -d '{
    "dataset_id": "dataset_123",
    "model_type": "stable_diffusion",
    "epochs": 10,
    "batch_size": 8,
    "learning_rate": 0.0001
  }'
```

### 5. Upload Custom Skills

```bash
curl -X POST http://localhost:8000/api/v1/skills/upload \
  -H "Content-Type: application/json" \
  -d '{
    "skill_name": "anime_art",
    "description": "Generate anime-style artwork",
    "prompt_template": "An anime character {subject} in {style} art style",
    "parameters": {
      "style": ["watercolor", "oil", "digital"],
      "subject": "string"
    },
    "category": "art_styles"
  }'
```

## API Endpoints

### Generation
- `POST /api/v1/generate` - Generate image from prompt
- `POST /api/v1/generate/batch` - Batch generate images
- `GET /api/v1/generate/{id}` - Get generation result
- `GET /api/v1/generations/history` - Get generation history

### Training
- `POST /api/v1/training/start` - Start training job
- `GET /api/v1/training/status/{job_id}` - Get training status
- `GET /api/v1/training/history` - Training history
- `POST /api/v1/training/cancel/{job_id}` - Cancel training
- `POST /api/v1/training/evaluate` - Evaluate model performance

### Skills
- `POST /api/v1/skills/upload` - Upload custom skill
- `GET /api/v1/skills/list` - List all skills
- `GET /api/v1/skills/{skill_id}` - Get skill details
- `PUT /api/v1/skills/{skill_id}` - Update skill
- `DELETE /api/v1/skills/{skill_id}` - Delete skill
- `POST /api/v1/skills/{skill_id}/use` - Use skill for generation

### Datasets
- `POST /api/v1/datasets/upload` - Upload dataset
- `GET /api/v1/datasets/list` - List datasets
- `GET /api/v1/datasets/{dataset_id}` - Get dataset info
- `DELETE /api/v1/datasets/{dataset_id}` - Delete dataset
- `POST /api/v1/datasets/{dataset_id}/validate` - Validate dataset
- `POST /api/v1/datasets/{dataset_id}/augment` - Data augmentation

### Analytics
- `GET /api/v1/analytics/usage` - API usage statistics
- `GET /api/v1/analytics/performance` - Model performance metrics
- `GET /api/v1/analytics/costs` - Cost tracking

## Supported Providers

### Current
- OpenAI DALL-E 3
- Stable Diffusion
- Midjourney

### Planned
- Leonardo.AI
- Adobe Firefly
- Google Imagen
- Replicate

## Self-Training System

The wrapper includes a sophisticated self-training system that:

1. **Learns from User Feedback**: Tracks which generated images are liked/disliked
2. **Fine-tunes Models**: Updates underlying models based on patterns
3. **Maintains Dataset Versions**: Keeps track of training data iterations
4. **Validates Improvements**: Measures performance gains
5. **Automated Retraining**: Schedules periodic retraining on accumulated data

## Skill System

Create reusable prompt templates with:
- Variable substitution
- Pre-defined parameter sets
- Version control
- Performance tracking
- Community sharing (optional)

## Dataset Management

- Upload datasets in JSON, CSV, or image formats
- Automatic validation and format conversion
- Data augmentation techniques
- Privacy and security controls
- Backup and versioning

## Configuration

See `.env.example` for all configurable options:

```bash
# API Keys
OPENAI_API_KEY=
STABLE_DIFFUSION_API_KEY=
MIDJOURNEY_API_KEY=

# Database
DATABASE_URL=postgresql://user:password@localhost/ai_image_gen

# Training
TRAINING_DEVICE=cuda  # or cpu
MAX_TRAINING_TIME=3600
BATCH_SIZE=8

# API
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=False
```

## Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_generation.py

# With coverage
pytest --cov=app tests/
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## Roadmap

- [ ] Multi-model ensemble support
- [ ] Advanced LoRA fine-tuning
- [ ] Web UI dashboard
- [ ] Mobile app
- [ ] Real-time collaboration
- [ ] Community skill marketplace
- [ ] Advanced analytics and reporting
- [ ] A/B testing framework
- [ ] Model quantization and optimization
- [ ] Distributed training support

## License

MIT License - see LICENSE file for details

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Join our community discord (link coming soon)

## Acknowledgments

- OpenAI for DALL-E API
- Stability AI for Stable Diffusion
- Midjourney for their amazing model
- PyTorch for deep learning framework
