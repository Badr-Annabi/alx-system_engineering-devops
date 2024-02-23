#This script installs flask

package { 'flask':
ensure          => 'present',
provider        => 'pip3',
install_options => ['==2.1.0'],
}
