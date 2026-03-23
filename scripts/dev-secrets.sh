
#!/bin/bash

export ACENDLY_DATABASE_NAME="db_acendly"
export ACENDLY_DATABASE_URL="postgresql+psycopg://postgres:$ACENDLY_DATABASE_PASSWORD@localhost:5432/$ACENDLY_DATABASE_NAME"
export ACENDLY_DATABASE_USERNAME="postgres"
export ACENDLY_DATABASE_PASSWORD="123456"
export DEV_TEST_KEY="43ce7d149e78837af37d93dc0f8b6ed6b8556431948936f892c898c07ee8ef4a0b3b764b8f6c61eb514d355eab29676ceee05d4159e8304e12c7120518c02456"
export ACENDLY_ENV="dev"
export ACENDLY_JWT_SECRET_KEY="3d32da8832dfb66d77e7a99c0a8f103860a72388e2397e32c261548233a80237966ad8d525e60d869276d0d92f8d1ed4dace98cef8bfda6356d973a7e6019d53"
export ACENDLY_KAFKA_SERVERS="localhost:9092"


# shellcheck disable=SC2028
echo "============================================"
echo "VNote Dev Environment Variables Setup Script"
echo "============================================"
echo ""
echo "✅ ACENDLY_DATABASE_NAME set"
echo "✅ ACENDLY_DATABASE_URL set"
echo "✅ ACENDLY_DATABASE_USERNAME set"
echo "✅ ACENDLY_DATABASE_PASSWORD set"
echo "✅ ACENDLY_ENV set"
echo "✅ ACENDLY_KAFKA_SERVERS set"
echo "✅ ACENDLY_JWT_SECRET_KEY set"
echo "✅ DEVELOPMENT TEST KEY set"

