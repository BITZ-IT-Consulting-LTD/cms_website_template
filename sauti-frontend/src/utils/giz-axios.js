import axios from 'axios';

const getBaseURL = () => {
    return 'https://backend.bitz-itc.com/api/';
};

// Create an Axios instance
const apiClient = axios.create({
    baseURL: getBaseURL(),
    timeout: 30000, // Increased timeout for file uploads
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdfaWQiOiJmZTNmZjM0OC04Y2Y0LTQ3MTktOTAxNy1hMGU3YjY2ZGUyMWIiLCJvcmdfbmFtZSI6IlRlc3QgT3JnYW5pemF0aW9uIDciLCJleHAiOjE3ODM2MzI3MzUsImlhdCI6MTc1MjA5NjczNSwianRpIjoiNTUyZTczNTYtY2Q0MC00ZjZhLTgyNGMtOWJiOGYyMmNlYmJkIn0.aCrjDD42fu-JpVtf7wkxlD1LZB6BpV63htWOpAdzvDw'
    }
});

// List of endpoints that don't require authentication
const publicEndpoints = [
    '/webhook/webform/',
    '/mglsd/reports/',
    '/public/',
    '/health',
    '/status'
];

// Check if URL is a public endpoint
const isPublicEndpoint = (url) => {
    return publicEndpoints.some(endpoint => url && url.includes(endpoint));
};

// Add a request interceptor
apiClient.interceptors.request.use(
    (config) => {
        console.log('API Request:', {
            method: config.method?.toUpperCase(),
            url: config.url,
            baseURL: config.baseURL,
            fullURL: `${config.baseURL}${config.url}`,
            isPublic: isPublicEndpoint(config.url)
        });

        // Handle authentication for different endpoint types
        if (isPublicEndpoint(config.url)) {
            console.log('Public endpoint detected');

            // For webform submissions, use specific token if needed
            if (config.url?.includes('/webhook/webform/')) {
                // Option 1: Use environment-specific token (Preferred)
                const webformToken = import.meta.env.VITE_APP_WEBFORM_TOKEN;

                if (webformToken) {
                    config.headers.Authorization = `Bearer ${webformToken}`;
                    console.log('Added webform token from environment to request');
                } else {
                    console.warn('No VITE_APP_WEBFORM_TOKEN found in environment variables. Webform submission may fail.');
                }
            }
            // For other public endpoints, no auth needed

            return config;
        }

        // For authenticated endpoints, try to get token from localStorage
        const token = localStorage.getItem('authToken');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
            console.log('Added auth token to request');
        } else {
            console.warn('No auth token found for authenticated endpoint');
        }

        return config;
    },
    (error) => {
        if (error.response) {
            switch (error.response.status) {
                case 401:
                    console.error('Unauthorized: Please log in again.');
                    localStorage.removeItem('authToken');
                    // window.location.href = '/login';
                    break;
                case 403:
                    console.error('Forbidden: Access denied.');
                    break;
                case 404:
                    console.error('Not Found: Resource not available.');
                    break;
                case 500:
                    console.error('Server Error: Try again later.');
                    break;
                default:
                    console.error(`Error: ${error.response.statusText}`);
            }
        }
        return Promise.reject(error);
    }
);

// Add a response interceptor
apiClient.interceptors.response.use(
    (response) => {
        console.log('API Response Success:', {
            status: response.status,
            statusText: response.statusText,
            url: response.config.url
        });
        return response;
    },
    (error) => {
        console.error('API Response Error:', {
            status: error.response?.status,
            statusText: error.response?.statusText,
            url: error.config?.url,
            data: error.response?.data
        });

        if (error.response) {
            const { status } = error.response;
            const isPublic = isPublicEndpoint(error.config?.url);

            switch (status) {
                case 401:
                    // Only redirect to login for authenticated endpoints
                    if (!isPublic) {
                        console.error('Unauthorized: Please log in again.');
                        localStorage.removeItem('authToken');
                        // Check if we're not already on login page to avoid redirect loops
                        if (!window.location.pathname.includes('/login')) {
                            window.location.href = '/login';
                        }
                    } else {
                        console.error('Unauthorized access to public endpoint - check API configuration');
                    }
                    break;

                case 403:
                    console.error('Forbidden: Access denied.');
                    // Don't redirect for public endpoints
                    if (!isPublic) {
                        // Could redirect to unauthorized page or show modal
                        console.warn('User does not have permission for this action');
                    }
                    break;

                case 404:
                    console.error('Not Found: Resource not available.');
                    break;

                case 422:
                    console.error('Validation Error:', error.response.data);
                    break;

                case 429:
                    console.error('Too Many Requests: Rate limit exceeded.');
                    break;

                case 500:
                    console.error('Server Error: Try again later.');
                    break;

                case 502:
                case 503:
                case 504:
                    console.error('Service Unavailable: Server is temporarily down.');
                    break;

                default:
                    console.error(`Error ${status}: ${error.response.statusText}`);
            }
        } else if (error.request) {
            // Network error
            console.error('Network Error: No response received from server');
        } else {
            // Request setup error
            console.error('Request Error:', error.message);
        }

        return Promise.reject(error);
    }
);

// Helper function to set auth token
export const setAuthToken = (token) => {
    if (token) {
        localStorage.setItem('authToken', token);
        apiClient.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    } else {
        localStorage.removeItem('authToken');
        delete apiClient.defaults.headers.common['Authorization'];
    }
};

// Helper function to clear auth
export const clearAuth = () => {
    localStorage.removeItem('authToken');
    delete apiClient.defaults.headers.common['Authorization'];
};

// Helper function to get current auth token
export const getAuthToken = () => {
    return localStorage.getItem('authToken');
};

// Helper function to check if user is authenticated
export const isAuthenticated = () => {
    const token = getAuthToken();
    return !!token;
};

export default apiClient;
